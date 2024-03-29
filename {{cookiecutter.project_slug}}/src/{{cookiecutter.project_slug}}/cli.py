import argparse
import logging

from . import {{ cookiecutter.project_slug }}
from . import commands

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = "WARNING"


def parse_args(argv):
    """Parse incoming arguments."""
    parser = argparse.ArgumentParser()
    parser.set_defaults(action=None)

    # Global arguments are defined here
    parser.add_argument(
        '-v', '--verbose', dest="log_level", action="append_const", const=-1,
        help="Increase verbosity (debug level) by one.",
    )
    parser.add_argument(
        '-q', '--quiet', dest="log_level", action="append_const", const=1,
        help="Decrease verbosity (debug level) by one.",
    )

    # Read in subcommands from the commands directory
    subparsers = parser.add_subparsers(
        title='Available subcommands',
        dest='command',
        help="Type 'sub-command -h' for more information.",
    )
    cmds = []
    cmds.append(commands.Hello())

    for cmd in cmds:
        cmd.add_subparser(subparsers)

    args = parser.parse_args(argv)

    log_level = LOG_LEVELS.index(DEFAULT_LOG_LEVEL)
    # For each "-q" and "-v" flag, adjust the logging verbosity accordingly
    # making sure to clamp off the value from 0 to 4, inclusive of both
    for adjustment in args.log_level or ():
        log_level = min(len(LOG_LEVELS) - 1, max(log_level + adjustment, 0))
    args.log_level = LOG_LEVELS[log_level]

    if args.action is None:
        parser.print_help()

    return args


def main(argv=None):
    args = parse_args(argv)

    logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=args.log_level)

    return {{ cookiecutter.project_slug }}.main(args)


if __name__ == '__main__':
    raise SystemExit(main())
