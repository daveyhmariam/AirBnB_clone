#!/usr/bin/python3
'''command interpreter entry for object interaction'''
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


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

    def emptyline(self):
        """
        The function "emptyline" does nothing and serves as a placeholder.
        """
        pass

    def do_create(self, arg):
        """
        The function `do_create` creates an object of a
        specified class, prints its ID, and saves it.
        """
        if arg:
            try:
                obj = globals()[arg]()
                print(obj.id)
                obj.save()
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, arg):
        """
        The function `do_show` takes an argument and checks if it
        """
        if arg:
            class_name = arg.split(" ")[0]
            key = arg.replace(' ', '.')

            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(arg.split(" ")) == 1:
                print("** instance id missing **")
            elif key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])
        else:
            print("** class name missing **")
        return

    def do_destroy(self, arg):
        """
        The function `do_destroy` takes an argument `arg`
        and checks if it is a valid class name and
        instance ID, and if so, deletes the instance from storage.
        """
        if arg:
            class_name = arg.split(" ")[0]
            key = arg.replace(' ', '.')

            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(arg.split(" ")) == 1:
                print("** instance id missing **")
            elif key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
        else:
            print("** class name missing **")
        return

    def do_all(self, arg):
        """
        The function `do_all` prints all objects in
        the storage that match the given argument, or all
        objects if no argument is provided.
        """
        if arg and arg not in globals().keys():
            print("** class doesn't exist **")
        else:
            if arg == "":
                print([str(value) for value in storage.all().values()])
            else:
                print([str(value) for value in storage.all().values()
                       if type(value).__name__ == arg])
        return

    def do_update(self, arg):
        """
        The function `do_update` updates the attribute
        value of an instance of a class based on the
        provided arguments.
        """
        if arg:
            value = arg.split(" ")
            class_name = value[0]
            key = value[0] + "."

            if class_name not in globals().keys():
                print("** class doesn't exist **")
            elif len(arg.split(" ")) == 1:
                print("** instance id missing **")
            elif key + value[1] not in storage.all().keys():
                print("** no instance found **")
            elif len(arg.split(" ")) == 2:
                print("* attribute name missing **")
            elif len(arg.split(" ")) == 3:
                print("** value missing **")
            else:
                key += value[1]
                if re.match(r'\d+$', value[3]):
                    attributeValue = int(value[3])
                elif re.match(r'\d+\.\d+', value[3]):
                    attributeValue = float(value[3])
                else:
                    attributeValue = value[3]

                setattr(storage.all()[key], value[2], attributeValue)
                storage.save()
        else:
            print("** class name missing **")
        return

    def do_count(self, arg):
        """
        The function `do_count` counts the number of
        values in `storage` that have a specific type name
        specified by the `arg` parameter.
        """
        count = 0
        for value in storage.all().values():
            if type(value).__name__ == arg:
                count += 1
        print(count)
        return

    def default(self, arg):
        """
        The function splits a string into words
        using a delimiter and then rearranges the words in a
        specific order before passing them
        as a command to another function.
        """
        # remember to handle ininite loop
        delimeter = r'[.,(){}:\'" ]+'
        args = re.split(delimeter, arg)
        result = ""

        if args[-1] == "":
            args.pop()

        if len(args) > 1:
            result = args[1] + " " + args[0]

        if len(args) > 2:
            for i in range(2, len(args)):
                result += " " + args[i]

        if result:
            self.onecmd(result)
        else:
            super().default(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
