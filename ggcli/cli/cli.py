from ggcli.cli.driver import CLIDriver
from ggcli.cli.driver2.driver2 import CLIDriver2


class CLI(object):

    def __init__(self, cli_driver=None):
        self.cli_driver = cli_driver
        if self.cli_driver == None:
            self.cli_driver = CLIDriver2()

    def run(self, args=None):
        self.cli_driver.main(args)
