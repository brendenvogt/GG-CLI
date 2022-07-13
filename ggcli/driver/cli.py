from ggcli import __version__
from ggcli.driver.loader import Loader
import argparse
from collections import OrderedDict
import copy
import sys


class CLIDriver(object):
    '''
    CLI Driver performs a few tasks for the CLI.
    1. Loads CLI metadata from data/cli.json
    2. constructs the data structures of the CLI such as arg table
    '''

    NAME_KEY = "name"
    DESCRIPTION_KEY = "description"
    SYNOPSIS_KEY = "synopsis"
    HELP_KEY = "help"
    OPTIONS_KEY = "options"
    COMMANDS_KEY = "commands"

    def __init__(self) -> None:
        self._cli_data = None
        self._command_table = None
        self._argument_table = None
        self._parser = None
        self.loader = Loader()
        self._get_cli_data()

        self._name = self._cli_data.get(
            self.NAME_KEY, None)
        self._description = self._cli_data.get(
            self.DESCRIPTION_KEY, None)
        self._synopsis = self._cli_data.get(
            self.SYNOPSIS_KEY, None)
        self._help = self._cli_data.get(
            self.HELP_KEY, None)
        self._options = self._cli_data.get(
            self.OPTIONS_KEY, None)
        self._commands = self._cli_data.get(
            self.COMMANDS_KEY, None)

        self._get_command_table()
        self._get_argument_table()
        self._get_parser()

    # CLI Data
    def _get_cli_data(self):
        if self._cli_data is None:
            self._cli_data = self.loader.load_data('cli')
        return self._cli_data

    # Argument Table
    def _get_argument_table(self):
        if self._argument_table is None:
            self._argument_table = self._build_argument_table()
        return self._argument_table

    def _build_argument_table(self):
        argument_table = OrderedDict()
        cli_arguments = self.options
        for option in cli_arguments:
            option_params = self._copy_kwargs(cli_arguments[option])
            cli_argument = self._create_cli_argument(option, option_params)
            argument_table[cli_argument.name] = cli_argument
        return argument_table

    def _copy_kwargs(self, kwargs):
        """
        This used to be a compat shim for 2.6 but is now just an alias.
        """
        copy_kwargs = copy.copy(kwargs)
        return copy_kwargs

    def _create_cli_argument(self, option_name, option_params):
        return CLIArgument(option_name, option_params)

    # Command Table
    def _get_command_table(self):
        if self._command_table == None:
            self._command_table = self._build_command_table()
        return self._command_table

    def _build_command_table(self):
        command_table = OrderedDict()
        commands = self._get_built_in_commands()  # todo BuiltIns and Plugins
        for command in commands:
            command = CLICommand(command=command)
            command_table[command.name] = command
        return command_table

    def _get_built_in_commands(self):
        return self._cli_data.get(self.COMMANDS_KEY)

    # Parser
    def _get_parser(self):
        if self._parser == None:
            self._parser = self._build_parser()
        return self._parser

    def _build_parser(self):
        parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.description,
            usage=self.synopsis
        )
        parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        parser.add_argument('--sum', dest='accumulate', action='store_const',
                            const=sum, default=max,
                            help='sum the integers (default: find the max)')

        parser.add_argument('--version', action='version', version=__version__)
        return parser

    def main(self, args=None):
        """
        :param args: List of arguments, with the 'root' removed.  For example,
            the command "ggcli xyz do-this --foo bar" will have an
            args list of ``['xyz', 'do-this', '--foo', 'bar']``.
        """
        if args is None:
            args = sys.argv[1:]
        command_table = self._get_command_table()
        argument_table = self._get_argument_table()
        parser = self._get_parser()
        args = parser.parse_args()
        print(f"command_table {command_table}")
        print(f"argument_table {argument_table}")
        # parsed_args, remaining = parser.parse_known_args(args)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def synopsis(self):
        return self._synopsis

    @property
    def help(self):
        return self._help

    @property
    def options(self):
        return self._options

    @property
    def commands(self):
        return self._commands


class CLICommand:
    NAME_KEY = "name"
    ALIAS_KEY = "alias"
    DESCRIPTION_KEY = "description"
    SYNOPSIS_KEY = "synopsis"
    SUBCOMMANDS_KEY = "subcommands"
    ARGUMENTS_KEY = "arguments"

    def __init__(self, command) -> None:
        self.name = command.get(self.NAME_KEY)
        self.alias = command.get(self.ALIAS_KEY)
        self.description = command.get(self.DESCRIPTION_KEY)
        self.synopsis = command.get(self.SYNOPSIS_KEY)
        self.subcommands = command.get(self.SUBCOMMANDS_KEY)
        self.arguments = command.get(self.ARGUMENTS_KEY)


class CLIArgument:
    HELP_KEY = 'help'
    DEST_KEY = 'dest'
    DEFAULT_KEY = 'default'
    ACTION_KEY = 'action'
    REQUIRED_KEY = 'required'
    CHOICES_KEY = 'choices'
    TYPE_KEY = 'type'

    def __init__(self, option_name, option_params) -> None:
        self.name = option_name
        self.help = option_params.get(self.HELP_KEY, '')
        self.dest = option_params.get(self.DEST_KEY)
        self.default = option_params.get(self.DEFAULT_KEY)
        self.action = option_params.get(self.ACTION_KEY)
        self.required = option_params.get(self.REQUIRED_KEY)
        self.choices = option_params.get(self.CHOICES_KEY)
        self.cli_type_name = option_params.get(self.TYPE_KEY)


class CLI(object):

    def __init__(self, cli_driver=None) -> None:
        # init cli driver
        self.cli_driver = cli_driver
        if self.cli_driver == None:
            self.cli_driver = CLIDriver()

    def main(self):
        self.cli_driver.main()
