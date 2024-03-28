#!/usr/bin/python3
"""command interpreter entry for object interaction"""

from models.base_model import BaseModel
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
        the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "FileStorage"]

    def do_quit(self, arg):
        """Exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """Exit the program
        
        Args:
            arg (str): command line argument
        """
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id

        Args:
            arg (str): command line argument
        """
        if len(arg.split()) == 0:
            print("** class name missing **")
            return
        if len(arg.split()) == 1:
            if arg.split()[0] not in type(self).__classes:
                print("** class doesn't exist **")
                return
            obj = globals()[arg.split()[0]]()
            print(obj.id)
            storage.save()
if __name__ == "__main__":
    HBNBCommand().cmdloop()
