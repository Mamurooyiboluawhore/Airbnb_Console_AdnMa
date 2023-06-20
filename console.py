#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
        prompt = "(hbnb) "
        __classes = {'BaseModel': BaseModel}

        def do_quit(self, args):
            """Quit command to exit the program
            """
            return True

        def do_EOF(self, args):
            """end of file command to exit the program
	    """
            return True

        def emptyline(self):
            """ A command to end last command 
            """
            pass
        def do_create(self, args):
            """ creates a new instance
            """
            if len(args) == 0:
                print("** class name missing **")

            elif args not in self.__classes:
                print("** class doesn't exist **")

            else:
                new_obj = self.__classes[args]()
                storage.save()
                print(f"{new_obj.id}")

        def do_show(self, args):
            """Prints the string representation
            """
            arg = args.split()
    
            if len(arg) == 0:
                print("** class name missing **")
            elif arg[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif f"{arg[0]}.{arg[1]}" not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[f"{arg[0]}.{arg[1]}"])

        
        def do_destroy(self, args):
            """Deletes an instance based on the class name and id
            """
            arg = args.split()
    
            if len(arg) == 0:
                print("** class name missing **")
            elif arg[0] not in self.__classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif f"{arg[0]}.{arg[1]}" not in storage.all():
                print("** no instance found **")
            else:
                del[storage.all()[f"{arg[0]}.{arg[1]}"]]
                storage.save()
        
        def do_all(self, args):

            if not args:
                print("** class name missing **")
            elif args not in self.__classes:
                print("** class doesn't exist **")
            elif args:
                objects = [str(v) for k, v in storage.all().items()]
                print(objects)
        
        def do_update(self, args):
            arg = args.split()

            if not arg:
                print("** class name missing **")
            elif arg[0] not in self.__classes:
                print("** class doesn't exist **")
            elif not arg[1]:
                print('** instance id missing **')
            elif f'{arg[0]}.{arg[1]}' not in storage.all():
                print("** no instance found **")
            elif not arg[2]:
                print("** attribute name missing **")
            elif not arg[3]:
                print("** value missing **")
            else:
                key = f'{arg[0]}.{arg[1]}'
                new_obj = storage.all().get(key)
                value = arg[3][1:-1]
                setattr(new_obj, arg[2], value)
                storage.save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()
