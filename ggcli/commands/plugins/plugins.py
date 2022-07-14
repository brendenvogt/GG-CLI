from ggcli.commands.command import CLICommand


def get_plugins():
    return [
        MySuperCoolPlugin()
    ]


class MySuperCoolPlugin(CLICommand):
    NAME = 'myplugin'
    DESCRIPTION = "test plugin description"
    SYNOPSIS = "ggcli myplugin <subcommand> [<Arg> ...]"
    SUBCOMMANDS = []

    def main(self, parsed_args, parsed_globals):
        print("hello world from plugins")
