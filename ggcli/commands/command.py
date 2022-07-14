from ggcli.cli.parser import CommandArgParser, SubcommandArgParser
from collections import OrderedDict


class BaseCommand(object):

    @property
    def name(self):
        return self.NAME

    NAME = ''
    DESCRIPTION = ''
    SYNOPSIS = ''
    ARG_TABLE = []
    SUBCOMMANDS = []
    EXAMPLES = []

    def __init__(self):
        self._arg_table = None
        self._subcommand_table = None

    def __call__(self, args, parsed_globals):
        return self.main(args, parsed_globals)

    def main(self, parsed_args, parsed_globals):
        # To be implemented by subclass.
        raise NotImplementedError("main")

    def create_help_command(self):
        # To be implemented by subclass.
        return None


class CLICommand(BaseCommand):
    SUBCOMMANDS = []

    def __init__(self):
        super().__init__()
        self._command_table = None
        self._name = ""

    def __call__(self, args, parsed_globals):
        service_parser = self._create_parser()
        parsed_args, remaining = service_parser.parse_known_args(args)
        command_table = self._get_command_table()
        return command_table[parsed_args.subcommand](remaining, parsed_globals)

    def _create_parser(self):
        command_table = self._get_command_table()
        # # Also add a 'help' command.
        # command_table['help'] = self.create_help_command()
        return CommandArgParser(
            subcommand_table=command_table, usage="", service_name=self._name)

    def _get_command_table(self):
        if self._command_table is None:
            self._command_table = self._create_command_table()
        return self._command_table

    def _create_command_table(self):
        command_table = OrderedDict()
        # service_model = self._get_service_model()
        for subcommand in self.SUBCOMMANDS:
            subcommand_name = subcommand.get("name")
            command_table[subcommand_name] = CLISubcommand(
                name=subcommand_name,
                parent_name=self._name
            )
        return command_table


class CLISubcommand(BaseCommand):

    def __init__(self, name, parent_name):
        super().__init__()
        self._name = name
        self._parent_name = parent_name

    def __call__(self, args, parsed_globals):
        argument_parser = self._create_parser()
        parsed_args, remaining = argument_parser.parse_known_args(args)
        print(f"Subcommand call {parsed_args}, remaining {remaining}")

    def _create_parser(self):
        argument_table = OrderedDict()
        return SubcommandArgParser(
            argument_table=argument_table, usage="")
