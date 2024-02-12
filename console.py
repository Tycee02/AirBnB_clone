#!/usr/bin/python3
"""
This is the console base for the airbnb
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Holberton command prompt to access models data"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Overrides default emptyline method"""
        pass

    def do_EOF(self, arg):
        """Close Interpreter and saves data, [CTR + D]"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
