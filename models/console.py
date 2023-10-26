#!/usr/bin/python3
"""Creates a basic command interpreter"""
import cmd
from models import base_models


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the interpreter"""
        return True

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if _name_ == '_main_':
    HBNBCommand().cmdloop()