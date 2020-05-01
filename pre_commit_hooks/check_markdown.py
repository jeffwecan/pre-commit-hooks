import argparse
import subprocess
from typing import Any, Generator, NamedTuple, Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        try:
            subprocess.check_call(('mdl', filename))
        except subprocess.CalledProcessError as exc:
            print(exc)
            retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
