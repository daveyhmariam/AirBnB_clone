#!/usr/bin/python3
"""command interpreter entry for object interaction"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
from models.place import Place
import json
import re
from models.review import Review
from models.state import State
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
        the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    __classes = ["Amenity",
                 "BaseModel",
                 "City",
                 "Place",
                 "Review",
                 "State",
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
        argp = arg.split(" ", 2)

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
            print("{}.{}".format(argp[0], argp[1]))
            print("** no instance found **")
            return False
        if len(argp) == 2:
            print("** attribute name missing **")
            return False
        if len(argp) == 3:
            if type(eval(argp[2])) != dict:
                print("** value missing **")
                return False
        if len(argp) == 4:
            obj = objects["{}.{}".format(argp[0], argp[1])]
            if argp[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argp[2]])
                obj.__dic__[argp[2]] = valtype(argp[3])
            else:
                obj.__dict__[argp[2]] = argp[3]
        else:
            obj = objects["{}.{}".format(argp[0], argp[1])]
            argp[2] = argp[2].replace("'", '"')
            argp[2] = json.loads(str(argp[2]))

            for k, v in argp[2].items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v


        storage.save()

    def default(self, arg: str):
        """
        The function splits a string into words using a delimiter and then rearranges the words in a specific order before passing them as a command to another function.

        Args:
            arg (str): The input string representing a command.
        """

        command_keywords = ["all", "create", "show", "destroy", "update", "count"]

        arg_keyword_match = re.search(r"[a-zA-Z.]+\(", arg)
        if arg_keyword_match:
            arg_keyword = arg_keyword_match.group()
        else:
            arg_keyword = None
        arg_keyword = arg_keyword.replace("(", "")
        arg_keyword = arg_keyword.split(".")[1] + " " + arg_keyword.split(".")[0]
        id_match = re.search(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", arg)
        if id_match:
            id_value = id_match.group()
        else:
            id_value = None

        para_match = re.search(r"\{[^{}]+\}", arg)
        if para_match:
            para_value = para_match.group()
            para_value = para_value.replace("'", "\"")
        else:
            para_value = None

        rearranged_command = ""
        if arg_keyword:
            rearranged_command += arg_keyword
        if id_value:
            rearranged_command += " " + id_value
        if para_value:
            rearranged_command += " " + para_value

        if (rearranged_command):
            self.onecmd(rearranged_command)
    def do_count(self, arg):
        """Update to command interpreter to retrieve
            the number of instances of a class: <class name>.count().

        Args:
            arg (str): command line value specifying class name
        """

        argp = arg.split()
        
        if not arg:
            print("** class name missing **")
            return False

        if argp[0] not in type(self).__classes:
            print("** class doesn't exist **")
            return False
        instances = 0
        objects = storage.all()
        for k in objects.keys():
            if argp[0] in k.split("."):
                instances += 1
        print(instances)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
