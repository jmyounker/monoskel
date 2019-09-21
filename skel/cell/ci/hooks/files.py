import os
import stat


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


def is_executable(path):
    return bool(os.stat(path).st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))


def has_ext(path):
    _, ext = os.path.splitext(os.path.basename(path))
    return ext != ""


def has_shebang(path):
    with open(path, "r") as f:
        return f.read(2) == "#!"
