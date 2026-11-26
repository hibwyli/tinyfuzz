"""4.3.3: exec each harness on seed inputs, drop chains with interpreter errors."""
import sys
import json
import ast
import pickle
import random
import string
from pathlib import Path

sys.path.insert(0, str(Path("cpython/Lib").resolve()))

seeds = ["192.0.2.1", "2001:db8::1", "192.0.2.0/24", 0, 3232235777,
         "", "not-an-ip", -1]

# ValueError is left out: ipaddress raises it on purpose (expected)
interpreter_errors = (TypeError, NameError, AttributeError, IndexError,
                      KeyError, ZeroDivisionError, SyntaxError)

data = json.loads(Path("data.json").read_text())

apisec = pickle.loads(Path("apisec.json").read_bytes())
observed_pool = []
for api in apisec["functions"] + [
    m for cls in apisec["classes"] for m in cls["functions"]
]:
    for values in api.get("input_values", {}).values():
        observed_pool.extend(values)


def reroll_args(source, attempt, i):
    random.seed(i * 10 + attempt)
    out = ""
    for line in source.splitlines(keepends=True):
        if not line.startswith("arg"):
            out += line
            continue
        head, sep, tail = line.partition("=")
        if not sep:
            out += line
            continue
        try:
            value = ast.literal_eval(tail.strip())
        except (ValueError, SyntaxError):
            out += line
            continue
        pool = [v for v in observed_pool if type(v) is type(value)]
        if pool and random.random() < 0.5:
            new = random.choice(pool)
        elif isinstance(value, bool):
            new = random.choice([True, False])
        elif isinstance(value, int):
            new = random.randint(-5, 1000)
        elif isinstance(value, float):
            new = random.uniform(-1000, 1000)
        elif isinstance(value, str):
            new = "".join(random.choices(string.printable,
                                         k=random.randint(0, 32)))
        else:
            out += line
            continue
        out += f"{head}= {new!r}\n"
    return out


valid = []
seen = set()
for i, block in enumerate(Path("harness.py").read_text().split("\n===\n")):
    source = ""
    for line in block.splitlines():
        if line.startswith("# Chain "):
            continue
        source += line + "\n"

    best = None
    for attempt in range(3):
        candidate = source if attempt == 0 else reroll_args(source, attempt, i)
        dropped = False
        covs = []
        for seed in seeds:
            lines_hit = set()

            def trace(frame, event, arg):
                if event == "line" and "ipaddress.py" in frame.f_code.co_filename:
                    lines_hit.add(frame.f_lineno)
                return trace

            sys.settrace(trace)
            try:
                exec(candidate, {"fuzz_input": seed})
            except Exception as e:
                if isinstance(e, interpreter_errors):
                    dropped = True
            finally:
                sys.settrace(None)
            covs.append(lines_hit)
            if dropped:
                break

        if dropped:
            continue
        if all(c == covs[0] for c in covs[1:]):
            continue
        best = candidate
        break

    if best is None:
        continue

    code = best.strip()
    if code in seen:
        continue
    seen.add(code)
    valid.append((i, code))
    print(f"Chain {i}: KEEP")

Path("valid_harness.py").write_text("\n\n===\n\n".join(
    f"# Chain {i}\n{code}" for i, code in valid))

fuzz = '''"""Atheris harness: one entry per valid tinyfuzz chain."""
import sys
from pathlib import Path
import atheris

with atheris.instrument_imports():
    sys.path.insert(0, str(Path("cpython/Lib").resolve()))
    import ipaddress

IGNORE = (ValueError, TypeError, AttributeError, OSError, LookupError,
          AssertionError, EOFError, ModuleNotFoundError, OverflowError,
          NameError, SyntaxError)


def decode(t, data):
    s = data.decode("utf-8", "replace")
    if s.startswith("%&$%"):
        s = s[4:].split("%&$%")[0]
    if t == "int":
        try:
            return int(s)
        except ValueError:
            return 0
    if t == "float":
        try:
            return float(s)
        except ValueError:
            return 0.0
    if t == "bool":
        return bool(s)
    return s


'''

for index, code in valid:
    fuzz_type = data[index]["fuzz_point"]["input_type"]
    fuzz += f"def chain_{index}(data):\n"
    fuzz += f"    fuzz_input = decode({fuzz_type!r}, data)\n"
    fuzz += "    try:\n"
    for line in code.splitlines():
        fuzz += "        " + line + "\n"
    fuzz += "    except IGNORE:\n        pass\n\n"

fuzz += "CHAINS = [" + ", ".join(f"chain_{i}" for i, _ in valid) + "]\n\n"
fuzz += """def TestOneInput(data):
    if not data:
        return
    CHAINS[data[0] % len(CHAINS)](data[1:])


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
"""
Path("fuzz.py").write_text(fuzz)
