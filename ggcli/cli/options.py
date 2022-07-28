

from argparse import ArgumentParser


class CLIOption:
    HELP_KEY = 'help'
    DEST_KEY = 'dest'
    DEFAULT_KEY = 'default'
    ACTION_KEY = 'action'
    REQUIRED_KEY = 'required'
    CHOICES_KEY = 'choices'
    TYPE_KEY = 'type'

    # TYPE_MAP = {
    #     'structure': str,
    #     'map': str,
    #     'timestamp': str,
    #     'list': str,
    #     'string': str,
    #     'float': float,
    #     'integer': str,
    #     'long': int,
    #     'boolean': bool,
    #     'double': float,
    #     'blob': str
    # }

    def __init__(self, option_name, option_params) -> None:
        self.name = option_name
        self.help = option_params.get(self.HELP_KEY, '')
        self.dest = option_params.get(self.DEST_KEY)
        self.default = option_params.get(self.DEFAULT_KEY)
        self.action = option_params.get(self.ACTION_KEY)
        self.required = option_params.get(self.REQUIRED_KEY)
        self.choices = option_params.get(self.CHOICES_KEY)
        self.cli_type_name = option_params.get(self.TYPE_KEY)

    # @property
    # def cli_type(self):
    #     return self.TYPE_MAP.get(self.cli_type_name, str)

    def add_to_parser(self, parser):
        pass
        # # parser.add_argument(
        # #     self.name,
        # #     help=self.help,
        # #     type=self.cli_type,
        # #     required=self.required)
        # parser.add_argument(self.name,
        #                     help=self.help)
