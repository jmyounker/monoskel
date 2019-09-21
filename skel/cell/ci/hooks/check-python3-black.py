"""Ensure that Python files pass flake8 checks.

    Usage: lint-python3-black [FILES]+

    Runs `black` on the requested files. Any failure results in a non-zero return code. Diffs
    are printed.

"""


import os
import sys

from cell.ci.hooks import files


def main(args):
    python_files = [x for x in args[1:] if files.is_python_file(x)]
    if not python_files:
        return 0
    os.execvp("black", ["black", "--check", "--diff"] + python_files)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
