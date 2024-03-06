#!/usr/bin/env python3
"""Defines all common attributes/methods for other classes"""
import uuid
import datetime

class BaseModel:
    """ base class for all the other classes on the project"""
    def __init__(self):
        """ Instantiation of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """ Prints a user freindly string representation of the object"""
        return "[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public intance attribute update_at with the
        with the current date time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of `__dict__`
        of the instance"""
        obj_dict_copy = self.__dict__.copy()
        obj_dict_copy['__class__'] = type(self).__name__
        obj_dict_copy['created_at'] = self.updated_at.isoformat()
        obj_dict_copy['updated_at'] = self.created_at.isoformat()
        return obj_dict_copy

    def __str__(self):
        """ prints a user friendly string representation of the object"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
