#!/usr/bin/python3
"""command interpreter entry for object interaction"""
import cmd


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
        the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program
        """
        return True

    def do_EOF(self, arg):
        """exit the program
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
