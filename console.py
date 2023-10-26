#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""
    
    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing when it recieves an empty line."""
        pass

    def do_quit(self, *args):
        """exits when typing quit."""
        return True

    def do_EOF(self, *args):
        """Exits on EOF."""
        print()
        return True
if __name__ == '__main__':
    
    HBNBCommand().cmdloop()
