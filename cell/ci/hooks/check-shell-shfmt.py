"""Ensure that shell scripts are correctly formatted.

    Usage: lint-shell [FILES]+

    Runs `shfmt` on the requested files. Diffs are displayed. Any
    failure results in a non-zero return code.

"""


import os
import subprocess
import sys

from cell.ci.hooks import files


def shell_dialect(path):
    """Returns None if not a shell and the shell variant otherwise. Variant may be posix or bash."""
    base, ext = os.path.splitext(os.path.basename(path))
    with open(path, "r") as f:
        first_line = f.readline(files.MAX_SHEBANG_LINE)  # Bounded but stupidly large
    if ext in [".zsh", ".fish"]:
        return None
    if not first_line.startswith("#!") and ext == ".sh":
        return "bash"
    if not first_line.startswith("#!"):
        return None
    if not files.is_executable(path):
        return None
    parts = first_line[2:].split()
    interpreter = os.path.basename(parts[0])
    if interpreter in ["ksh", "sh"]:
        return "posix"
    elif interpreter in ["bash", "dash"]:
        return "bash"
    else:
        return None


def shfmt(path, dialect):
    """Lints the appropriate dialect. Returns none if lint passed, otherwise the diff."""
    cmd = ["shfmt", "-ln", dialect, "-d", "-i", "4", path]
    p = subprocess.run(cmd, stdin=subprocess.PIPE, capture_output=True)
    if p.returncode == 0:
        return None
    return {
        "fix": "shfmt -ln %s -i 4 %s" % (dialect, os.path.abspath(path)),
        "diff": p.stdout.decode("utf8"),
    }


def main(args):
    path_dialect = ((x, shell_dialect(x)) for x in args[1:])
    lintable_path_dialect = ((x, dialect) for x, dialect in path_dialect if dialect is not None)
    # As an optimization we could partition by dialect and the running shfmt on those batches
    path_lint = ((x, shfmt(x, dialect)) for x, dialect in lintable_path_dialect)
    unclean_path_lint = [(x, lint) for x, lint in path_lint if lint is not None]
    for path, lint in unclean_path_lint:
        sys.stderr.write("error: script %s is unclean\n" % path)
        sys.stderr.write("fix with: %s\n" % lint["fix"])
        sys.stderr.write(lint["diff"])
    return 1 if unclean_path_lint else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
