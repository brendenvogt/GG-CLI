

class Command():
    def __init__(self, name, short_name=None, index=None, subcommands=[], help="") -> None:
        self.name = name
        self.short_name = short_name
        self.index = index
        self.subcommands = subcommands
        self.help = help


class Subcommand():

    def __init__(self, name, short_name=None, func=None, help="") -> None:
        self.name = name
        self.short_name = short_name
        self.func = func
        self.help = help


class Argument():
    # TODO
    def __init__(self) -> None:
        pass


class Option():
    def __init__(self, name, short_name=None, nargs=0, func=None) -> None:
        self.name = name
        self.short_name = short_name
        self.nargs = nargs
        self.func = func
