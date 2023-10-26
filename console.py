#!/usr/bin/python3
"""Command interpreter for HBnB"""
import cmd

from models.base_model import BaseModel

from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBnB"""
    
<<<<<<< HEAD
    prompt = '(hbnb) '

=======
    prompt = '(hbnb)'
    Doc_header = "(type help <topic>):"
    def emptyline(self):
        """Does nothing when it recieves an empty line."""
        pass
>>>>>>> 2a59c0469a962ce0f74e2e0b658e8dcf875f2e60

    def do_quit(self, *args):
        """exits when typing quit."""
        return True

    def do_EOF(self, *args):
        """Exits on EOF."""
        print()
        return True
<<<<<<< HEAD

    def emptyline(self):
        """Does nothing when it recieves an empty line."""
        pass


if __name__ == '__main__':
=======
        if __name__ == '__main__':
>>>>>>> 2a59c0469a962ce0f74e2e0b658e8dcf875f2e60
    HBNBCommand().cmdloop()
