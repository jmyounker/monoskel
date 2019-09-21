"""Ensure that executable files don't have file extensions.

    Usage: check-exe-have-no-ext [FILES]+

    If any files are executable and have file extensions then it returns
    with a non-zero exit code. Prints diagnostics to stderr.

"""


import os
import sys

from cell.ci.hooks import files


def main(args):
    executables = (x for x in args[1:] if not os.path.isdir(x) and files.is_executable(x))
    executables_with_ext = [x for x in executables if files.has_ext(x)]
    for exe in executables_with_ext:
        sys.stderr.write("error: script %s is not executable\n" % exe)
    return 1 if executables_with_ext else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
