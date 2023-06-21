#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage():
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return self.__objects

	def new(self, obj):
		key = f"{obj.__class__.__name__}.{obj.id}"
		self.__objects[key] = obj

	def save(self):
		with open(self.__file_path, "w", encoding="utf-8") as f:
			newDict = {}
			for k, v in self.__objects.items():      
				newDict[f"{k}"] = v.to_dict()
			json.dump(newDict, f)

	def reload(self):
		try:
			with open(self.__file_path, "r", encoding="utf-8") as f:
				r = json.load(f)
				for v in r.values():
					o = v["__class__"]
					eval(o)(**v)
		except:
			pass
