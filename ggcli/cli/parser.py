import argparse


class CommandAction(argparse.Action):

    def __init__(self, option_strings, dest, command_table, **kwargs):
        self.command_table = command_table
        super(CommandAction, self).__init__(
            option_strings, dest, choices=self.choices, **kwargs
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)

    @property
    def choices(self):
        return list(self.command_table.keys())

    @choices.setter
    def choices(self, val):
        pass


class CLIArgParser(argparse.ArgumentParser):
    pass


class MainArgParser(CLIArgParser):
    Formatter = argparse.RawTextHelpFormatter

    def __init__(self, command_table, version_string,
                 description, option_table, usage, prog=None):
        super(MainArgParser, self).__init__(
            formatter_class=self.Formatter,
            add_help=False,
            conflict_handler='resolve',
            description=description,
            usage=usage,
            prog=prog)
        self._build(command_table, version_string, option_table)

    def _create_choice_help(self, choices):
        help_str = ''
        for choice in sorted(choices):
            help_str += '* %s\n' % choice
        return help_str

    def _build(self, command_table, version_string, option_table):
        for option_name in option_table:
            option = option_table[option_name]
            option.add_to_parser(self)
        self.add_argument('--version', action="version",
                          version=version_string,
                          help='Display the version of this tool')
        self.add_argument('--debug', action="store_true",
                          help='Display the version of this tool')
        self.add_argument('command', action=CommandAction,
                          command_table=command_table)


class CommandArgParser(CLIArgParser):

    def __init__(self, subcommand_table, usage, service_name):
        super(CommandArgParser, self).__init__(
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=False,
            conflict_handler='resolve',
            usage=usage)
        self._build(subcommand_table)
        self._service_name = service_name

    def _build(self, subcommand_table):
        self.add_argument('subcommand', action=CommandAction,
                          command_table=subcommand_table)


class SubcommandArgParser(CLIArgParser):
    def __init__(self, argument_table, usage, command_table=None):
        super(SubcommandArgParser, self).__init__(
            add_help=False,
            usage=usage,
            conflict_handler='resolve')
        if command_table is None:
            command_table = {}
        self._build(argument_table, command_table)

    def _build(self, argument_table, command_table):
        for arg_name in argument_table:
            argument = argument_table[arg_name]
            argument.add_to_parser(self)
        if command_table:
            self.add_argument('argument', action=CommandAction,
                              command_table=command_table, nargs='?')

    def parse_known_args(self, args, namespace=None):
        if len(args) == 1 and args[0] == 'help':
            namespace = argparse.Namespace()
            namespace.help = 'help'
            return namespace, []
        else:
            return super(SubcommandArgParser, self).parse_known_args(args, namespace)
