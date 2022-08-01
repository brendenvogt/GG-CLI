import logging
from ggcli.cli.driver2 import command_provider
from ggcli.cli.driver2 import option_provider
import sys
from ggcli.cli.driver2 import argparser
LOG = logging.getLogger(__name__)


class CLIDriver2():

    def __init__(self) -> None:

        # Options
        self.option_table = option_provider.instance.get()
        print("Found options:")
        for option_name, option in self.option_table.items():
            print(f"- {option_name}")

        # Commands
        self.command_table = command_provider.instance.get()
        print("Found commands and subcommands:")
        for command, subcommands in self.command_table.items():
            print(f"- {command}")
            for subcommand in subcommands:
                print(f"  - {subcommand.name}")

        self.parser = argparser.ArgParser(description="An argparse example")
        self.parser.add_argument(
            '-f', '--foo', help='description', required=False, default="asfd", type=str)
        self.parser.add_argument('--debug', action='store_true')

# The add_argument() method
# ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
# Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

# name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
# action - The basic type of action to be taken when this argument is encountered at the command line.
# nargs - The number of command-line arguments that should be consumed.
# const - A constant value required by some action and nargs selections.
# default - The value produced if the argument is absent from the command line and if it is absent from the namespace object.
# type - The type to which the command-line argument should be converted.
# choices - A container of the allowable values for the argument.
# required - Whether or not the command-line option may be omitted (optionals only).
# help - A brief description of what the argument does.
# metavar - A name for the argument in usage messages.
# dest - The name of the attribute to be added to the object returned by parse_args().

    def main(self, args):
        args = vars(self.parser.parse_args())
        print(args)
