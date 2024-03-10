#!/usr/bin/env python3
""" Defines a class that contains the entry point of the command
    of the command interpreter"""
from cmd import Cmd
from models.base_model import BaseModel
import shlex

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
