#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
	and DBStorage
"""


from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
# from base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

storage.reload()
