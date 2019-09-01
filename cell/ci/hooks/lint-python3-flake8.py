"""Ensure that Python files pass flake8 checks.

    Usage: lint-python3-flake8 [FILES]+

    Runs `flake8` on the requested files. Any failure results in a non-zero return code.

"""


import os
import sys


MAX_SHEBANG_LINE = 10000


def is_python_file(path):
    """True if `path` is a Python file. False otherwise."""
    if path.endswith(".py"):
        return True
    with open(path, "r") as f:
        first_line = f.readline(MAX_SHEBANG_LINE)  # Bounded but stupidly large
    if not first_line.startswith("#!"):
        return False
    return "python3" in first_line[2:]


def find_in_path(predicate, path):
    if predicate(path):
        return path
    dirname, basename = os.path.split(path)
    if dirname == path:
        return None
    return find_in_path(predicate, dirname)


def contains_file(filename):
    def predicate(path, filename=filename):
        return os.path.exists(os.path.join(path, filename))

    return predicate


def main(args):
    python_files = [x for x in args[1:] if is_python_file(x)]
    if not python_files:
        return 0
    root = find_in_path(contains_file("pyproject.toml"), os.path.abspath(args[0]))
    if root is None:
        return 1
    config = os.path.join(root, "pyproject.toml")
    os.execvp("flake8", ["flake8", "--config", config] + python_files)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
