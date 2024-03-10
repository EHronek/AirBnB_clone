#!/usr/bin/env python3
""" Defines a class that contains the entry point of the command
    of the command interpreter"""
from cmd import Cmd
from models.base_model import BaseModel
import shlex
from models import storage

classes = {'BaseModel': BaseModel}


class HBNBCommand(Cmd):
    """ entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF to Exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it to JSON
            and prints the `id` """
        parsed_args = shlex.split(arg)
        try:
            if not arg:
                print('** class name missing **')
            elif arg not in globals():
                print("** class doesn't exist **")
            elif parsed_args[0] in classes:
                obj = classes[parsed_args[0]]()
                print(obj.id)
                obj.save()
            
        except Exception:
            pass

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        based on the class name and id """
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
            return False
        if parsed_args[0] in classes:
            if len(parsed_args) > 1:
                key = parsed_args[0] + '.' + parsed_args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print('** no instance found **')
            else:
                print('** instance id missing **')
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            save the changes in the json file"""
        parsed_args = shlex.split(arg)
        if len(parsed_args) == 0:
            print('** class name missing **')
        elif parsed_args[0] in classes:
            if len(parsed_args) > 1:
                key = parsed_args[0] + '.' + parsed_args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print('** class doesn\'t exist **')

    def do_all(self, arg):
        """ Prints all string representation of all instances based
        based or not on the class name"""
        parsed_args = shlex.split(arg)
        obj_list = []
        if len(parsed_args) == 0:
            for value in storage.all().values():
                obj_list.append(str(value))
        elif parsed_args[0] in classes:
            for key in storage.all():
                if parsed_args[0] in storage.all():
                    obj_list.append(str(storage.all()[key]))
        else:
            print('** class doesn\'t exist **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
