from copy_files.cli import get_args
from copy_files.copy_files import copy
import sys
from copy_files.log import setup


def main():
    """Launch copy_files cli.

    Returns:
        Return cli.
    """
    path, log = get_args()
    setup(loglevel=log)
    try:
        copy(path)
    except OSError:
        sys.exit(1)


if __name__ == '__main__':
    main()
