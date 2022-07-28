'''
print out the version to the console and return
'''
from ggcli import __version__


def main():
    print(f"{__version__}")


def help():
    return "Prints out the application version to the console"


def alias():
    return "v"
