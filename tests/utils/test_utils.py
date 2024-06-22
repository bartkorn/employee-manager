import io
import sys


def stdout_capture(func, *args, **kwargs):
    """
    Captures standard output contents from a given function call and returns them
    """
    captured_output = io.StringIO()
    sys.stdout = captured_output

    match len(args):
        case 0:
            func()
        case 1:
            func(args[0])
        case other:
            func(args)

    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()
