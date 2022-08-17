from typing import List, Any


class Argument():
    def __init__(self, name: str, type: type, positional: bool, default: Any = None, help=None, short_name: str = None) -> None:
        self.name = name
        self.type = type
        self.positional = positional
        self.default = default
        self.help = help
        self.short_name = short_name


class OptionalArgument(Argument):
    def __init__(self, name: str, type: type, default: Any = None, help=None, short_name=None):
        super(OptionalArgument, self).__init__(
            name, type, False, default, help, short_name)


class PositionalArgument(Argument):
    def __init__(self, name: str, type: type, default: Any = None, help=None):
        super(PositionalArgument, self).__init__(
            name, type, True, default, help)


class Subcommand():

    def __init__(self, name, short_name=None, func=None, help="", arguments: List[Argument] = []) -> None:
        self.name = name
        self.short_name = short_name
        self.func = func
        self.help = help
        self.arguments = arguments


class Command():
    def __init__(self, name, short_name=None, index=None, subcommands: List[Subcommand] = [], help="", arguments: List[Argument] = []) -> None:
        self.name = name
        self.short_name = short_name
        self.index = index
        self.subcommands = subcommands
        self.help = help
        self.arguments = arguments


class Option():
    def __init__(self, name, short_name=None, nargs=0, func=None) -> None:
        self.name = name
        self.short_name = short_name
        self.nargs = nargs
        self.func = func
