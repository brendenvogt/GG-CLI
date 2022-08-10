from ggcli.cli.models import Command, Subcommand


def foobar_main(args):
    print(f"foobar_main: {args}")


command = Command(
    name="foo",
    short_name="f",
    subcommands=[
        Subcommand(
            name="bar",
            short_name="b",
            func=foobar_main,
            help="This is the good old 'foo bar' function"
        )
    ],
    help="This is the good old 'foo' function"
)
