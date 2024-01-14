#!/usr/bin/python3
"""the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """inheris the cmd.Cmd class
    """
    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

    def do_quit(self, line):
        """exits the command line"""
        return True
    def do_EOF(self, line):
        """exits the command line"""
        return True
    def emptyline(self, line) -> bool:
        return super().emptyline()

if __name__ == '__main__':
    HBNBCommand().cmdloop()