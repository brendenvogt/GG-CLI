class Command:
    def __init__(self, name, main, help, alias) -> None:
        self.name = name
        self.main = main
        self.help = help
        self.alias = alias

    def run(self, args):
        self.main(args)
