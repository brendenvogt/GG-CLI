'''
sets the debug flag to true and enables debug logging
'''
import os


def main(args):
    # set debug to true
    # get option name
    filename = os.path.basename(__file__)
    option_name = os.path.splitext(filename)[0]
    args[option_name] = True


def help():
    return "sets the debug flag to true and enables debug logging"


def example():
    return "ggcli --debug"
