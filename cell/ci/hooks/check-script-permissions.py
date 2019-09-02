"""Ensure that files with shebang lines are executable.

    Usage: check-script-permissions [FILES]+

    If any files have shebang lines but are not executable then this script
    exits with non-zero exit code. Prints diagnostics to stderr.

"""


import os
import sys

from cell.ci.hooks import files


def main(args):
    scripts = [x for x in args[1:] if not os.path.isdir(x) and files.has_shebang(x)]
    bad_scripts = [x for x in scripts if not files.is_executable(x)]
    for script in bad_scripts:
        sys.stderr.write("error: script %s is not executable\n" % script)
    return 1 if bad_scripts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
