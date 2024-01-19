import argparse
import logging

from . import {{ cookiecutter.project_slug }}

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = "WARNING"


def parse_args(argv):
    """Parse incoming arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-v', '--verbose', dest="log_level", action="append_const", const=-1,
        help="Increase verbosity (debug level) by one.",
    )
    parser.add_argument(
        '-q', '--quiet', dest="log_level", action="append_const", const=1,
        help="Decrease verbosity (debug level) by one.",
    )

    args = parser.parse_args(argv)

    log_level = LOG_LEVELS.index(DEFAULT_LOG_LEVEL)
    # For each "-q" and "-v" flag, adjust the logging verbosity accordingly
    # making sure to clamp off the value from 0 to 4, inclusive of both
    for adjustment in args.log_level or ():
        log_level = min(len(LOG_LEVELS) - 1, max(log_level + adjustment, 0))
    args.log_level = LOG_LEVELS[log_level]

    return args


def main(argv=None):
    args = parse_args(argv)

    logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=args.log_level)

    return {{ cookiecutter.project_slug }}.main(args)


if __name__ == '__main__':
    raise SystemExit(main())
