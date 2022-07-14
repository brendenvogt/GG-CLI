from ggcli.cli.driver import CLIDriver


class CLI(object):

    def __init__(self, cli_driver=None) -> None:
        self.cli_driver = cli_driver
        if self.cli_driver == None:
            self.cli_driver = CLIDriver()

    def run(self):
        self.cli_driver.main()
