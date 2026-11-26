"""4.3.3: exec each harness on seed inputs, drop chains with interpreter errors."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path("cpython/Lib").resolve()))

seeds = ["192.0.2.1", "2001:db8::1", "192.0.2.0/24", 0, 3232235777,
         "", "not-an-ip", -1]

# ValueError is left out: ipaddress raises it on purpose (expected)
interpreter_errors = (TypeError, NameError, AttributeError, IndexError,
                      KeyError, ZeroDivisionError, SyntaxError)

valid = []
seen = set()
for i, block in enumerate(Path("harness.py").read_text().split("\n===\n")):
    source = ""
    for line in block.splitlines():
        if line.startswith("# Chain "):
            continue
        source += line + "\n"

    dropped = False
    for seed in seeds:
        try:
            exec(source, {"fuzz_input": seed})
        except Exception as e:
            if isinstance(e, interpreter_errors):
                print(f"Chain {i}: DROP - {type(e).__name__} on seed {seed!r}")
                dropped = True
                break

    if not dropped:
        code = source.strip()
        if code in seen:
            continue
        seen.add(code)
        valid.append(f"# Chain {i}\n{code}")
        print(f"Chain {i}: KEEP")

Path("valid_harness.py").write_text("\n\n===\n\n".join(valid))
