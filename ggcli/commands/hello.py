from ggcli.cli.models import Command, OptionalArgument, PositionalArgument, Subcommand, Argument


def hello_main(args):
    prefix = args.prefix+' ' if args.prefix is not None else ''
    suffix = ' '+args.suffix if args.suffix is not None else ''
    print(f"hello {prefix}{args.firstname} {args.lastname}{suffix}")


def helloworld_main(args):
    print(f"hello world: {args}")


def hello_brenden(args):
    print(f"Hello Brenden its nice to see you again")


command = Command(
    name="hello",
    index=hello_main,
    arguments=[
        Argument(
            name="prefix",
            type=str,
            required=False,
            # default="Mr",
            help="optional arg"
        ),
        PositionalArgument(
            name="firstname",
            type=str,
            # default="Brenden",
            help="required arg"
        ),
        PositionalArgument(
            name="lastname",
            type=str,
            # default="Vogt",
            help="required arg"
        ),
        OptionalArgument(
            name="suffix",
            type=str,
            # default="The First",
            help="optional arg"
        )
    ],
    subcommands=[
        # Subcommand(
        #     name="world",
        #     func=helloworld_main,
        #     help="Ah the wonderful 'hello world' function"
        # ),
        # Subcommand(
        #     name="brenden",
        #     func=hello_brenden,
        #     help="a hello just for Brenden"
        # ),
    ],
    help="This is the good old 'hello' function"
)
