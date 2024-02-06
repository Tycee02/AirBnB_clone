#!/usr/bin/python3
"""
This is the console base for the airbnb
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Holberton command prompt to access models data"""

    intro = "Welcome to the AirBnB Console"
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Close Interpreter and saves data, [CTR + D]"""
        print("")
        return True

    def do_quit(self, arg):
        """Close de Interpreter and saves data"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
