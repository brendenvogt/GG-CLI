class BaseCommand(object):

    @property
    def name(self):
        raise NotImplementedError("name")

    @name.setter
    def name(self, value):
        raise NotImplementedError("name")

    @property
    def arg_table(self):
        return {}

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


class CLISubcommand(BaseCommand):
    PARENT = ''
