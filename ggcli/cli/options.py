

from argparse import ArgumentParser


class CLIOption:
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

    def add_to_parser(self, parser):
        pass
