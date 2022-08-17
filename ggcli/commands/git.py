from ggcli.cli.models import Command, OptionalArgument, PositionalArgument, Subcommand, Argument


def add(args):
    print(f"Adding file(s) {args.file}")


def commit(args):
    print(
        f"Committing with provided message of: {args.message} and args {args}")


def push(args):
    print("Pushing changes")


def pull(args):
    print("Pushing latest")


def log(args):
    print("Showing log")


def status(args):
    print("Showing status")


command = Command(
    name="git",
    arguments=[
        OptionalArgument(
            name="global",
            type=bool,
            default=True,
            help="Stores whether the command should be applied globally. (this is just a fake test argument)"
        )
    ],
    subcommands=[
        Subcommand(
            name="add",
            func=add,
            arguments=[
                PositionalArgument(
                    name="file",
                    type=str,
                    help="The path or paths you want to stage"
                )
            ]
        ),
        Subcommand(
            name="commit",
            func=commit,
            arguments=[
                OptionalArgument(
                    short_name="m",
                    name="message",
                    type=str,
                    help="The message you want to commit with"
                )
            ]
        ),
        Subcommand(
            name="push",
            func=push
        ),
        Subcommand(
            name="pull",
            func=pull
        ),
        Subcommand(
            name="status",
            func=status
        ),
        Subcommand(
            name="log",
            func=log),
    ]
)
