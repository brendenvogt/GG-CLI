import logging
from ggcli.cli.provider import command_provider
from ggcli.cli.provider import option_provider
from ggcli.cli import argparser
from ggcli.cli import data
from ggcli import __version__

LOG = logging.getLogger(__name__)


def test_subcommand(args):
    print(f"subcommand: {args}")


def test_index(args):
    print(f"index: {args}")


class Command():
    def __init__(self, name, short_name=None, index=None, subcommands=[], help="") -> None:
        self.name = name
        self.short_name = short_name
        self.index = index
        self.subcommands = subcommands
        self.help = help


class Subcommand():

    def __init__(self, name, short_name=None, func=None, help="") -> None:
        self.name = name
        self.short_name = short_name
        self.func = func
        self.help = help


class CLIDriver():

    def __init__(self) -> None:

        # CLI Data
        self.data = data.CLIData()
        # print(f"name: {self.data.name}")
        # print(f"description: {self.data.description}")
        # print(f"synopsis: {self.data.synopsis}")
        # print(f"help: {self.data.help}")

        # Options
        self.option_table = option_provider.instance.get()
        # print("Found options:")
        # for option_name, option in self.option_table.items():
        #     print(f"- {option_name}")

        # Commands
        self.command_table = command_provider.instance.get()
        # print("Found commands and subcommands:")
        # for command, subcommands in self.command_table.items():
        #     print(f"- {command}")
        #     for subcommand in subcommands:
        #         print(f"  - {subcommand.name}")

        self.parser = argparser.ArgParser(
            prog=self.data.name,
            description=self.data.description,
            usage=self.data.synopsis
        )

        # Add global flags and options
        self.parser.add_argument(
            '--debug', action='store_true')
        self.parser.add_argument(
            '--version', action='version', version=f'{__version__}')

        commands_table = [
            Command(
                name="foo",
                short_name="f",
                subcommands=[
                    Subcommand(
                        name="bar",
                        short_name="b",
                        func=test_subcommand,
                        help="This is the good old 'foo bar' function"
                    )
                ],
                help="This is the good old 'foo' function"
            ),
            Command(
                name="hello",
                index=test_index,
                subcommands=[
                    Subcommand(
                        name="world",
                        func=test_subcommand,
                        help="Ah the wonderful 'hello world' function"
                    )
                ],
                help="This is the good old 'hello' function"
            ),
        ]

        # if theres commands
        if len(commands_table) > 0:
            # Add a commands subparser
            commands_parsers = self.parser.add_subparsers(title='Top Level Commands',
                                                          description='Please enter a valid top level command.',
                                                          help='commands help')
            # For each command in the commands table
            for command in commands_table:
                # Get the short names
                command_aliases_list = [
                    command.short_name] if command.short_name is not None else []
                # Create a command parser for our specific command
                command_parser = commands_parsers.add_parser(
                    command.name,
                    aliases=command_aliases_list,
                    help=command.help)
                # If theres an index function
                if command.index:
                    # Attach it to the command parser
                    command_parser.set_defaults(func=command.index)
                # If theres subcommands
                if command.subcommands and len(command.subcommands) > 0:
                    # Create a subcommands subparser
                    subcommands_parsers = command_parser.add_subparsers(title=f'Subcommands for \"{command.name}\"',
                                                                        description='Please type a valid subcommand',
                                                                        help='additional help')
                    # For each subcommand
                    for subcommand in command.subcommands:
                        # Create the short name list
                        subcommand_aliases_list = [
                            subcommand.short_name] if subcommand.short_name is not None else []
                        # Create the subcommand parser
                        subcommand_parser = subcommands_parsers.add_parser(
                            subcommand.name,
                            aliases=subcommand_aliases_list,
                            help=subcommand.help)
                        # If theres a subcommand func
                        if subcommand.func:
                            # Attach it to the subcommand parser
                            subcommand_parser.set_defaults(
                                func=subcommand.func)


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
        args = self.parser.parse_args()
        try:
            if "func" in args:
                func = args.func
                func(args)
            else:
                print(args)
                self.parser.parse_args(['-h'])
        except AttributeError as e:
            self.parser.error(f"{e}")
