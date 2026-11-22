import inspect
import sys
from collections import defaultdict
from pathlib import Path


input_types = defaultdict(lambda: defaultdict(set))
output_types = defaultdict(set)



def tracer(frame, event, arg):
    api_id = (
        str(Path(frame.f_code.co_filename).resolve()),
        getattr(frame.f_code, "co_qualname", frame.f_code.co_name),
    )

    # we get this through the namespace sharing
    if api_id[0] != TRACE_TARGET_FILE:
        return tracer

    if event == "call":
        arg_info = inspect.getargvalues(frame)

        for parameter in arg_info.args:
            if parameter in ("self", "cls"):
                continue

            value = arg_info.locals[parameter]
            input_types[api_id][parameter].add(
                type(value).__name__
            )

    elif event == "return":
        if isinstance(arg, tuple):
            output_types[api_id].add(
                ("tuple", tuple(type(item).__name__ for item in arg))
            )
        else:
            output_types[api_id].add(type(arg).__name__)

    return tracer

sys.settrace(tracer)
