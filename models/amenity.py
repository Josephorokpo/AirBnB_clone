#!/usr/bin/python3
"""
Module containing the Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class with a name attribute.

    Public class attributes:
    - name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Amenity class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
