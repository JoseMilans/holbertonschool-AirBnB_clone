import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    CLASS_NAME_MAP = {
        "BaseModel": "models.base_model.BaseModel",
        "User": "models.user.User",
        "State": "models.state.State",
        "City": "models.city.City",
        "Place": "models.place.Place",
        "Review": "models.review.Review",
        "Amenity": "models.amenity.Amenity"
    }

    def __init__(self, file_path="file.json"):
        self.__file_path = file_path
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dict_to_save = {key: obj.to_dict()
                            for key, obj in self.__objects.items()}
            json.dump(dict_to_save, f, indent=4)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                seri_objs = json.load(f)
                for key, value in seri_objs.items():
                    class_name = value["__class__"]
                    cls_path = self.CLASS_NAME_MAP.get(class_name)
                    if cls_path:
                        module_name, class_name = cls_path.rsplit('.', 1)
                        module = __import__(module_name, fromlist=[class_name])
                        cls = getattr(module, class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance
