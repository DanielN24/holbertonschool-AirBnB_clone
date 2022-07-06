#!/usr/bin/python3
"""
    File Storage class.
"""


import json


class FileStorage():
    """
    FileStorage class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the class attribute __object """
        return FileStorage.__objects

    def new(self, obj):
        """
            Creates a new class.id & value of an
            instance in __objects dictionary
        """
        if obj is not None:
            key_name = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key_name] = obj.to_dict()

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = {}
        for key in FileStorage.__objects:
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(new_dict, f)
        """
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump({key: value.to_dict() for key, value in
                        FileStorage.__objects.items()}, f)
        """
        

    def reload(self):
        """
            Deserializes the JSON file to __objetcs
        """
        from ..amenity import Amenity
        from ..base_model import BaseModel
        from ..city import City
        from ..place import Place
        from ..review import Review
        from ..state import State
        from ..user import User

        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                file_obj = json.load(f).items
                for (key, value) in file_obj:
                    eval(value["__class__"])(**value)

        except Exception:
            pass
