from ggcli.cli.loader import Loader


class CLIData(object):

    NAME_KEY = "name"
    DESCRIPTION_KEY = "description"
    SYNOPSIS_KEY = "synopsis"
    HELP_KEY = "help"
    OPTIONS_KEY = "options"

    def __init__(self) -> None:
        self._loader = Loader()
        self._cli_data = None
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

    def _get_cli_data(self):
        if self._cli_data is None:
            self._cli_data = self._loader.load_data('cli')
        return self._cli_data

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
