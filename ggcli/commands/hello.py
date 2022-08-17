from ggcli.cli.models import Command, Subcommand


def hello_main(args):
    print(f"hello: {args}")


def helloworld_main(args):
    print(f"hello world: {args}")


def hello_brenden(args):
    print(f"Hello Brenden its nice to see you again")


command = Command(
    name="hello",
    index=hello_main,
    subcommands=[
        Subcommand(
            name="world",
            func=helloworld_main,
            help="Ah the wonderful 'hello world' function"
        ),
        Subcommand(
            name="brenden",
            func=hello_brenden,
            help="a hello just for Brenden"
        ),

    ],
    help="This is the good old 'hello' function"
)
