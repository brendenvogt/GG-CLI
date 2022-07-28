'''
sets the debug flag to true and enables debug logging
'''
import os


def main(args):
    # set debug to true
    # get option name
    filename = os.path.basename(__file__)
    option_name = os.path.splitext(filename)[0]
    print(f"args: {args}")
    print(f"setting option {option_name}")
    flags = dict()
    flags[option_name] = True
    print(flags)
    # do something
    # return mutated state
    # Get global state singleton
    return {flags}


def help():
    return "sets the debug flag to true and enables debug logging"


def example():
    return "ggcli --debug"
