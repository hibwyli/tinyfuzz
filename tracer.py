import inspect
import sys
from collections import defaultdict


input_types = defaultdict(lambda: defaultdict(set))
output_types = defaultdict(set)


def tracer(frame, event, arg):
    function = frame.f_code.co_name

    if event == "call":
        arg_info = inspect.getargvalues(frame)

        for parameter in arg_info.args:
            if parameter in ("self", "cls"):
                continue

            value = arg_info.locals[parameter]
            input_types[function][parameter].add(
                type(value).__name__
            )

    elif event == "return":
        output_types[function].add(
            type(arg).__name__
        )

    return tracer

sys.settrace(tracer)
