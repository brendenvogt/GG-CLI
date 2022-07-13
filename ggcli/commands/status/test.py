from ggcli.commands.basic import CLISubcommand


class TestSubcommand(CLISubcommand):
    PARENT = 'status'
    NAME = 'test'
    DESCRIPTION = "test command description"
    SYNOPSIS = "ggcli status test [<Arg> ...]"
