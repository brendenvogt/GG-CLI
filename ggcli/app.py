from ggcli.cli.cli import CLI
import sys


def run():
    cli = CLI()
    args = sys.argv[1:]
    cli.run(args)


if __name__ == "__main__":
    run()
