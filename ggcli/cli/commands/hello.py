from ggcli.cli.models import Command, Subcommand


def hello_main(args):
    print(f"hello: {args}")


def helloworld_main(args):
    print(f"hello world: {args}")


command = Command(
    name="hello",
    index=hello_main,
    subcommands=[
        Subcommand(
            name="world",
            func=helloworld_main,
            help="Ah the wonderful 'hello world' function"
        )
    ],
    help="This is the good old 'hello' function"
)
