"""Ensure that Python files pass flake8 checks.

    Usage: lint-python3-flake8 [FILES]+

    Runs `flake8` on the requested files. Any failure results in a non-zero return code.

"""


import os
import sys

from cell.ci.hooks import files


def main(args):
    python_files = [x for x in args[1:] if files.is_python_file(x)]
    if not python_files:
        return 0
    root = files.find_in_path(files.contains_file("pyproject.toml"), os.path.abspath(args[0]))
    if root is None:
        return 1
    config = os.path.join(root, "pyproject.toml")
    print(os.environ["PATH"])
    os.execvp("flake8", ["flake8", "--config", config] + python_files)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
