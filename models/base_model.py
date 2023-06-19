#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():

	def __init__(self, *args, **kwargs):
		if kwargs:
			del kwargs["__class__"]
			if kwargs["updated_at"]:
				kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])
			if kwargs ["created_at"]:
				kwargs["created_at"] = datetime.fromisoformat(kwargs["created_at"])
			for k, v in kwargs.items():
				setattr(self, k, v)

		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

    
	def __str__(self):
		return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		dictcopy = self.__dict__.copy()
		dictcopy['__class__'] = self.__class__.__name__
		dictcopy['created_at'] = self.created_at.isoformat()
		dictcopy['updated_at'] = self.updated_at.isoformat()
		return dictcopy
