#!/usr/bin/python3
"""command interpreter entry for object interaction"""

from models.base_model import BaseModel
import cmd
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
        the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "User"]

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

    def do_show(self, arg):
        """Prints the string representation of
            an instance based on the class name

        Args:
            arg (str): consists the class and object id
        """
        objects = storage.all()
        argp = arg.split()
        if len(argp) == 0:
            print("** class name missing **")
            return
        if argp[0] not in type(self).__classes:
            print("** class doesn't exist **")
            return
        if len(argp) == 1:
            print("** instance id missing **")
            return
        if ("{}.{}".format(argp[0], argp[1])
                not in objects.keys()):
            print("** no instance found **")
            return
        print(objects["{}.{}".format(argp[0], argp[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Args:
            arg (str): consists the class and object id
        """

        objects = storage.all()
        argp = arg.split()
        if len(argp) == 0:
            print("** class name missing **")
            return
        if argp[0] not in type(self).__classes:
            print("** class doesn't exist **")
            return
        if len(argp) == 1:
            print("** instance id missing **")
            return
        if ("{}.{}".format(argp[0], argp[1])
                not in objects.keys()):
            print("** no instance found **")
            return
        del (objects["{}.{}".format(argp[0], argp[1])])
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
            instances based or not on the class name.

        Args:
            arg (str): consists the class
        """
        argp = arg.split()
        objects = storage.all()
        if len(argp) == 0:
            for v in objects.values():
                print(v)
            return False
        if argp[0] not in type(self).__classes:
            print("** class doesn't exist **")
        else:
            if argp[0] in type(self).__classes:
                for k in objects.keys():
                    if k.split(".")[0] == argp[0]:
                        print(objects[k])

    def do_update(self, arg):
        """Updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file)

        Args:
            arg (str): <class name> <id> <attribute name> "<attribute value>"
        """
        objects = storage.all()
        argp = arg.split()

        if len(argp) == 0:
            print("** class name missing **")
            return False
        if argp[0] not in type(self).__classes:
            print("** class doesn't exist **")
            return False
        if len(argp) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argp[0], argp[1]) not in objects.keys():
            print("** no instance found **")
            return False 
        if len(argp) == 2:
            print("** attribute name missing **")
            return False
        if len(argp) == 3:
            print("** value missing **")
            return False
        print(len(argp))
        if len(argp) == 4:
            obj = objects["{}.{}".format(argp[0], argp[1])]
            if argp[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argp[2]])
                obj.__dic__[argp[2]] = valtype(argp[3])
            else:
                obj.__dict__[argp[2]] = argp[3]

        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
