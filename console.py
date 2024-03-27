#!/usr/bin/python3
"""command interpreter entry for object interaction"""
import cmd


class HBNBCommand(cmd.Cmd):
    '''The `HBNBCommand` class is a command-line interface
    for managing objects in a storage system.'''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''exit the command interpreter'''
        return True

    def do_EOF(self, arg):
        '''exit the command interpreter by using control-D'''
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
