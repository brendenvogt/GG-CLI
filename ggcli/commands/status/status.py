from ggcli.commands.basic import CLICommand
from ggcli.commands.status.test import TestSubcommand


class Status(CLICommand):
    NAME = 'status'
    DESCRIPTION = "Status command description"
    SYNOPSIS = "ggcli status <subcommand> [<Arg> ...]"
    SUBCOMMANDS = [
        {'name': 'test', 'command_class': TestSubcommand},
    ]

    def main(self, parsed_args, parsed_globals):
        print("main from Status command")
