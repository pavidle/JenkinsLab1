from commands import *
from sys import argv


def get_executor(subcommand=None):
    commands = {
        'fill': fill,
        'init': init,
        f'show {subcommand}': show
    }
    return commands


def execute(command):
    command.pop(0)
    length = len(command)
    command = " ".join(command)
    if length == 0:
        show_help()
        return
    if length == 2:
        subcommand = command.split()[1]
        get_executor(subcommand)[command](subcommand)
    else:
        get_executor()[command]()


try:
    execute(argv)
except KeyError:
    show_help()
