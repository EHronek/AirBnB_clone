#!/usr/bin/env python3
""" Defines a class storage that serializes instances to a json file
    and desirializes JSON file to instances"""
import json


class FileStorage:
    """serializes instances to json file and desirializes json file
    to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to json file (path: __file_path)"""
        with open(self.__file_path, 'w') as js_file:
            json.dump(self.__objects, js_file)

    def reload(self):
        """ Deserializes the json file to __objects (only if the JSON
        file(__file_path) exists: otherwise, do nothing. If the file
        doesn't exist, no exemption should be raised"""
        try:
            with open(self.__file_path, 'r') as js_file:
                self.__objects = json.load(js_file)
        except:
            pass
