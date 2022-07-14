from ast import parse
from ggcli import __version__
from ggcli.cli.data import CLIData
from ggcli.cli.options import CLIOption
from collections import OrderedDict
from ggcli.commands.plugins import plugins
from ggcli.commands.builtins import builtins
from ggcli.cli.parser import MainArgParser
import copy
import argparse
import sys
import logging

LOG = logging.getLogger(__name__)


class CLIDriver(object):
    '''
    CLI Driver performs a few tasks for the CLI.
    1. Loads CLI metadata from data/cli.json
    2. Load Built in commands
    2. constructs the data structures of the CLI such as arg table
    '''

    def __init__(self) -> None:
        # CLI Data - loaded from the data/cli.json file. Responsible for high level data like name, description, but also options definitions.
        self._cli_data = CLIData()

        # Options - build options table
        self._options_table = None
        self._get_options_table()

        # Commands - load built in commands
        self._command_table = None
        self._get_command_table()

        # Plugins - load plugins
        self._plugins = None
        self._get_plugins_table()

        # Parser - create parser
        self._parser = None
        self._get_parser()

    # Options Table

    def _get_options_table(self):
        if self._options_table is None:
            self._options_table = self._build_options_table()
        return self._options_table

    def _build_options_table(self):
        options_table = OrderedDict()
        options = self._cli_data.options
        for option in options:
            option_params = self._copy_kwargs(options[option])
            cli_option = CLIOption(option, option_params)
            options_table[cli_option.name] = cli_option
        return options_table

    def _copy_kwargs(self, kwargs):
        """
        This used to be a compat shim for 2.6 but is now just an alias.
        """
        copy_kwargs = copy.copy(kwargs)
        return copy_kwargs

    def _get_command_table(self):
        if self._command_table is None:
            self._command_table = self._build_command_table()
        return self._command_table

    def _build_command_table(self):
        command_table = OrderedDict()
        for builtin in builtins.get_builtins():
            command_table[builtin.name] = builtin
        return command_table

    # Plugins
    def _get_plugins_table(self):
        if self._plugins == None:
            self._plugins = self._build_plugin_table()
        return self._plugins

    def _build_plugin_table(self):
        plugins_list = plugins.get_plugins()
        for plugin in plugins_list:
            self._command_table[plugin.name] = plugin
        return plugins_list

    # Parser

    def _get_parser(self):
        if self._parser == None:
            self._parser = self._build_parser()
        return self._parser

    def _build_parser(self):
        parser = MainArgParser(
            command_table=self._command_table,
            version_string=__version__,
            prog=self._cli_data.name,
            description=self._cli_data.description,
            usage=self._cli_data.synopsis,
            option_table=self._options_table
        )
        return parser

    def main(self, args=None):

        # Get Args - gets everything after ggcli
        if args is None:
            args = sys.argv[1:]

        # Parse Args
        parsed_args, remaining = self._parser.parse_known_args(args)
        self._handle_options(parsed_args)

        LOG.debug(f"parsed_args {parsed_args}")
        LOG.debug(f"remaining {remaining}")
        return self._command_table[parsed_args.command](remaining, parsed_args)

    def _handle_options(self, parsed_args):
        if parsed_args.debug:
            logging.basicConfig(level=logging.DEBUG)
            LOG.debug("Debug mode enabled")
