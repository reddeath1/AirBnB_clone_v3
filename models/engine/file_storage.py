#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        self._FileStorage__objects = None

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        _dict = {}
        for key, val in FileStorage.__objects.items():
            if isinstance(val, cls):
                _dict[key] = val
        return _dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """public instance method to delete obj from __objects
        if it’s inside
        """
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def get(self, cls, id):
        """Method to retrieve one object
        Return the object based on the class name and its ID, or
        None if not found
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is None:
            return None
        for item in self.__objects.values():
            if item.__class__ == cls and item.id == id:
                return item

    def count(self, cls=None):
        """A method to count the number of objects in storage
        Returns the number of objects in storage matching the given class name
        If no name is passed, returns the count of all objects in storage
        """
        if type(cls) is str:
            cls = classes.get(cls)
        if cls is None:
            return len(self.all())

            return len(self.all(cls))

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def all(self, cls=None):
        """returns the object dictionary ( __dict)"""
        if not cls:
            return self.__objects
        elif type(cls) == str:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls}
        else:
            return {k: v for k, v in self.__objects.items()
                    if v.__class__ == cls}
