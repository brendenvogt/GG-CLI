from ggcli.commands.command import CLICommand
from ggcli.commands.mybuiltin.test import TestSubcommand


class MySuperCoolBuiltin(CLICommand):
    NAME = 'mybuiltin'
    DESCRIPTION = "Status command description"
    SYNOPSIS = "ggcli mybuiltin <subcommand> [<Arg> ...]"
    SUBCOMMANDS = [
        {'name': 'test', 'command_class': TestSubcommand},
    ]

    def main(self, parsed_args, parsed_globals):
        print("main from mybuiltin command")
