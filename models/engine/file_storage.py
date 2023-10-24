#!/usr/bin/python3
"""
FileStorage class for serialisation and deserialisation of instances.
"""
import json
import os
BaseModel = None


class FileStorage:
    """
    Serialises instances to a JSON file & deserialises back to instances
    """

    __file_path = "file.json"  # path to json file
    __objects = {}  # dictionary to store objects
    CLASS_NAME_MAP = {
        "BaseModel": "models.base_model.BaseModel"
        # space to add more classes
    }

    def all(self):
        """Return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add the object to the dictionary with a formatted key"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialise the __objects to JSON file."""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            dict_to_save = {key: obj.to_dict()
                            for key, obj in FileStorage.__objects.items()}
            json.dump(dict_to_save, f)

    def reload(self):
        """Deserialise the JSON file to __objects, if the file exists."""
        global BaseModel
        if BaseModel is None:
            # importing BaseModel only if not already loaded
            from models.base_model import BaseModel
        if os.path.exists(FileStorage.__file_path):
            # load the serialised objects from the file
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    class_name = value["__class__"]
                    # get the module and class path from mapping
                    cls_path = FileStorage.CLASS_NAME_MAP.get(class_name)
                    if cls_path:
                        # extract module and class names from the path
                        module_name, class_name = cls_path.rsplit('.', 1)
                        # import the module and extract the class
                        module = __import__(module_name, fromlist=[class_name])
                        cls = getattr(module, class_name)
                        # create new instance of the class with serialised data
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance