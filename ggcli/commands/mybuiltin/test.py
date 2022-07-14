from ggcli.commands.command import CLISubcommand


class TestSubcommand(CLISubcommand):
    NAME = 'test'
    DESCRIPTION = "test command description"
    SYNOPSIS = "ggcli status test [<Arg> ...]"
