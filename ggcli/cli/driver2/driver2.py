import logging
from ggcli.cli.driver2 import command_provider
from ggcli.cli.driver2 import option_provider

LOG = logging.getLogger(__name__)


class CLIDriver2():

    def __init__(self) -> None:

        self.command_table = command_provider.instance.get()
        print("Found commands and subcommands:")
        for command, subcommands in self.command_table.items():
            print(f"- {command}")
            for subcommand in subcommands:
                print(f"  - {subcommand.name}")
                # print(subcommand.help())
        self.option_table = option_provider.instance.get()
        print("Found Options:")
        for option_name, option in self.option_table.items():
            print(f"- {option_name}")

    def main(self, args):
        pass
