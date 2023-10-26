#!/usr/bin/python3
"""Initialises and sets up the storage process"""

from models.engine.file_storage import FileStorage

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

dict_class = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
    'State': State
}

storage = file_storage.FileStorage()
storage.reload()
