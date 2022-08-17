import logging
from ggcli.cli import data
from ggcli import __version__
import argparse
from ggcli.options.all import options_table
from ggcli.commands.all import commands_table
from ggcli.cli.models import Command

LOG = logging.getLogger(__name__)


class BasicAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super().__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if self.nargs == 0:
            setattr(namespace, self.dest, True)
        if self.nargs > 0:
            setattr(namespace, self.dest, values)


class CLIDriver():

    def _has_subcommands(self, command: Command) -> bool:
        return command.subcommands and len(command.subcommands) > 0

    def __init__(self) -> None:

        # CLI Data
        self.data = data.CLIData()

        self.parser = argparse.ArgumentParser(
            prog=self.data.name,
            description=self.data.description,
            usage=self.data.synopsis
        )

        for option in options_table:
            names = [f"--{option.name}"]
            short_name = f"-{option.short_name}" if option.short_name else None
            if short_name:
                names.append(short_name)
            self.parser.add_argument(
                *names, action=BasicAction, nargs=option.nargs, default=None)

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
                    # Add arguments. But complaining about positional args if there are subcommands present.
                for arg in command.arguments:
                    if (arg.positional):
                        if self._has_subcommands(command):
                            print(
                                f"Detected positional args and subcommands, which is not supported. Ignoring the position argument: {arg.name}")
                            continue
                        command_parser.add_argument(
                            arg.name, type=arg.type, help=arg.help, nargs=None if arg.default is None else '?', default=arg.default)
                    else:
                        if (arg.type is bool):
                            command_parser.add_argument(
                                f'-{arg.short_name if arg.short_name is not None else arg.name}', f'--{arg.name}', dest=arg.name, type=arg.type, help=arg.help, default=arg.default, action=argparse.BooleanOptionalAction)
                        else:
                            command_parser.add_argument(
                                f'-{arg.short_name if arg.short_name is not None else arg.name}', f'--{arg.name}', dest=arg.name, type=arg.type, help=arg.help, default=arg.default)
                    # TODO probably conflict between subcommands and required index arguments
                # If theres subcommands
                if self._has_subcommands(command):
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
                            for arg in subcommand.arguments:
                                if (arg.positional):
                                    subcommand_parser.add_argument(
                                        arg.name, type=arg.type, help=arg.help, nargs=None if arg.default is None else '?', default=arg.default)
                                else:
                                    if (arg.type is bool):
                                        subcommand_parser.add_argument(
                                            f'-{arg.short_name if arg.short_name is not None else arg.name}', f'--{arg.name}', dest=arg.name, type=arg.type, help=arg.help, default=arg.default, action=argparse.BooleanOptionalAction)
                                    else:
                                        subcommand_parser.add_argument(
                                            f'-{arg.short_name if arg.short_name is not None else arg.name}', f'--{arg.name}', dest=arg.name, type=arg.type, help=arg.help, default=arg.default)

    def main(self, args):
        args = self.parser.parse_args()
        try:
            if args.version:
                print(__version__)
                return
            if args.debug:
                print("DEBUG MODE ACTIVATED")
            if args.verbose:
                print(
                    f"VERBOSE MODE ACTIVATED to the level of {len(args.verbose)}")
            if "func" in args:
                func = args.func
                func(args)
            else:
                print(args)
                self.parser.parse_args(['-h'])
        except AttributeError as e:
            self.parser.error(f"{e}")
