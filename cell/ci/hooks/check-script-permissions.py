"""Ensure that files with shebang lines are executable.

    Usage: check-script-permissions [FILES]+

    If any files have shebang lines but are not executable then this script
    exits with non-zero exit code. Prints diagnostics to stderr.

"""


import os
import stat
import sys


def has_shebang(path):
    with open(path, "r") as f:
        return f.read(2) == "#!"


def is_executable(path):
    return bool(os.stat(path).st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))


def main(args):
    scripts = [x for x in args[1:] if not os.path.isdir(x) and has_shebang(x)]
    bad_scripts = [x for x in scripts if not is_executable(x)]
    for script in bad_scripts:
        sys.stderr.write("error: script %s is not executable\n" % script)
    return 1 if bad_scripts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
