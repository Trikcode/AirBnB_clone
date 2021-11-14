#!/usr/bin/python3
"""command line interpreter"""
import cmd
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'
    class_name = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']

    def emptyline(self):
        """do not execute last command with empty line"""
        pass

    def do_quit(self, line):
        """quits"""
        raise SystemExit

    def do_EOF(self, line):
        """end of file"""
        print('')
        return True

    def do_create(self, line):
        """make a new instance"""
        if line in self.class_name:
            if line == "BaseModel":
                new_obj = BaseModel()
            elif line == "User":
                new_obj = User()
            elif line == "State":
                new_obj = State()
            elif line == "City":
                new_obj = City()
            elif line == "Amenity":
                new_obj = Amenity()
            elif line == "Place":
                new_obj = Place()
            elif line == "Review":
                new_obj = Review()
            new_obj.save()
            print(new_obj.id)
        elif line:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show instance of class and id"""
        args = line.split(" ")
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            show_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if show_key in all_obj:
                print(all_obj[show_key])
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """delete instance based on class and id"""
        args = line.split(" ")
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            dest_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if dest_key in all_obj:
                del all_obj[dest_key]
                storage.save()
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """print all instances or all class instances"""
        if line in self.class_name:
            all_obj = storage.all()
            all_int = []
            for keys in all_obj.keys():
                if line == all_obj[keys].__class__.__name__:
                    all_int.append(str(all_obj[keys]))
            print(all_int)
        elif line:
            print("** class doesn't exist **")
        else:
            all_obj = storage.all()
            all_int = []
            for keys in all_obj.keys():
                all_int.append(str(all_obj[keys]))
            print(all_int)

    def do_update(self, line):
        """add or update attribute"""
        args = shlex.split(line)
        try:
            args[0]
        except IndexError:
            print("** class name missing **")
            return
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            update_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if update_key in all_obj:
                try:
                    args[2]
                except IndexError:
                    print("** attribute name missing **")
                    return
                try:
                    args[3]
                except IndexError:
                    print("** value missing **")
                    return
                if (args[2] == 'my_number' or args[2] == 'number_rooms' or
                        args[2] == 'number_bathrooms' or args[2] ==
                        'max_guest' or args[2] == 'price_by_night'):
                    setattr(all_obj[update_key], args[2], int(args[3]))
                elif args[2] == 'latitude' or args[2] == 'longitude':
                    setattr(all_obj[update_key], args[2], float(args[3]))
                else:
                    setattr(all_obj[update_key], args[2], str(args[3]))
                setattr(all_obj[update_key], 'updated_at', datetime.now())
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
