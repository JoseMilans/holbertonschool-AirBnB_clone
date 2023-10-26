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

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            dict_to_save = {key: obj.to_dict()
                            for key, obj in FileStorage.__objects.items()}
            json.dump(dict_to_save, f, indent=4)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                seri_objs = json.load(f)
                for key, value in seri_objs.items():
                    class_name = value["__class__"]
                    cls_path = FileStorage.CLASS_NAME_MAP.get(class_name)
                    if cls_path:
                        module_name, class_name = cls_path.rsplit('.', 1)
                        module = __import__(module_name, fromlist=[class_name])
                        cls = getattr(module, class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
