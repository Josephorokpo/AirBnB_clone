#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for common attributes/methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                            self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                            )
                elif key != '__class__':
                    setattr(self, key, value)
            # If it's a new instance, add it to storage and call new method
            if 'id' not in kwargs:
                storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Add the new instance to storage and call new method
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the
        current datetime. Calls the save method of storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self, **kwargs):
        """
        Returns a dictionary representation of the BaseModel instance.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__

        # Include additional arguments in the dictionary
        for key, value in kwargs.items():
            obj_dict[key] = value

        return obj_dict
