from ggcli.cli.models import Option


def test_index(args):
    print(f"Test Args: {args}")


options_table = [
    Option(name="debug", short_name="d", nargs=0, func=test_index),
    Option(name="version", nargs=0, func=test_index),
    Option(name="verbose", short_name="v", nargs=3, func=test_index),
    Option(name="stage", nargs=1),
    Option(name="domain", nargs=1),
    Option(name="realm", nargs=1)
]
