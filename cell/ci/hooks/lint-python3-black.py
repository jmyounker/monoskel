"""Ensure that Python files pass flake8 checks.

    Usage: lint-python3-black [FILES]+

    Runs `black` on the requested files. Any failure results in a non-zero return code. Diffs
    are printed.


"""


import os
import sys


MAX_SHEBANG_LINE = 1024


def is_python_file(path):
    """True if `path` is a Python file. False otherwise."""
    if path.endswith(".py"):
        return True
    with open(path, "r") as f:
        first_line = f.readline(MAX_SHEBANG_LINE)  # Bounded but stupidly large
    if not first_line.startswith("#!"):
        return False
    return "python3" in first_line[2:]


def main(args):
    python_files = [x for x in args[1:] if is_python_file(x)]
    if not python_files:
        return 0
    os.execvp("black", ["black", "--check", "--diff"] + python_files)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
