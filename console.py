#!/usr/bin/python3
"""the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


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

    def emptyline(self):
        """EOF signal to exit the program."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
           saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
            return
        else:
            try:
                obj = eval(line)()
                print(obj.id)
                obj.save()
                return
            except (NameError, KeyError):
                print("** class doesn't exist **")
        return

    def do_show(self, line):
        """"Prints the string representation of
            an instance based on the class name and id
        """
        if line:
            cls_name = line.split(" ")[0]
            if len(line.split(" ")[0]) > 1:
                key = line.replace(" ", ".")
            if cls_name not in globals().keys():
                print("** class doesn't exist **")
                return
            if len(line.split(" ")) == 1:
                print("** instance id missing **")
                return
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                print(storage.all()[key])
        else:
            print("** class name missing **")
        return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line:
            cls_name = line.split(" ")[0]
            if len(line.split(" ")[0]) > 1:
                key = line.replace(" ", ".")
            if cls_name not in globals().keys():
                print("** class doesn't exist **")
                return
            if len(line.split(" ")) == 1:
                print("** instance id missing **")
                return
            if key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                del storage.all()[key]
                storage.save()
        else:
            print("** class name missing **")
            return

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name.
        """
        if line and line not in globals().keys():
            print("** class doesn't exist **")
        else:
            if line is None or line == "":
                print([str(value) for value in storage.all().values()])
            else:
                print([str(value) for value in storage.all().values()
                       if line == type(value).__name__])
        return

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating
           attribute (save the change into the JSON file)"""
        if not line or line == "":
            print("** class name missing **")
            return
        else:
            if len(line.split(" ")) == 1:
                if line not in globals().keys():
                    print("** class doesn't exist **")
                    return
                else:
                    print("** instance id missing **")
                    return
            elif len(line.split(" ")) == 2:
                if line.replace(" ", ".") not in storage.all().keys():
                    print("** no instance found **")
                    return
                else:
                    print("** attribute name missing **")
                    return
            elif len(line.split(" ")) == 3:
                print("** value missing **")
            else:
                arg_list = line.split(" ")
                key = arg_list[0] + "." + arg_list[1]
                name = arg_list[2]
                value = arg_list[3]
                value = type(storage.all()[key].to_dict()[name])(value)
                obj = storage.all()[key]
                setattr(obj, name, value)
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
