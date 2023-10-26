#!/usr/bin/python3
"""Creates a basic command interpreter"""
import cmd
from models import base_models
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the interpreter"""
        print()
        return True

    def do_quit(self, arg):
        """Exit the interpreter"""
        return True

    def emptyline(self):
        """Passing emptyline do nothing"""
        pass
    if not line:
            print("** class name missing **")
    elif line not in self.classes:
            print("** class doesn't exist **")
    else:
            new_item = eval(line)()
            print(new_item.id)
            new_item.save()

if _name_ == '_main_':
    HBNBCommand().cmdloop()
