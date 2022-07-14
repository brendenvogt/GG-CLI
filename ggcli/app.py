from ggcli import __version__
from ggcli.cli.cli import CLI


def run():
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    run()
