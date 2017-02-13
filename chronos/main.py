import argcomplete

from chronos.constants import HelpOnErrorArgumentParser
from chronos.scheduler import create_dep, create, delete, graph, kill, list, search, start


def main():
    parser = HelpOnErrorArgumentParser()
    subparsers = parser.add_subparsers(parser_class=HelpOnErrorArgumentParser, help='Description')

    for sub_command in [create_dep, create, delete, graph, kill, list, search, start]:
        sub_command.register_command(subparsers)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args.func(args)
