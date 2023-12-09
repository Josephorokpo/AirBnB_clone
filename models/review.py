#!/usr/bin/python3
"""
Module containing the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class with place_id, user_id, and text attributes.

    Public class attributes:
    - place_id: string - empty string: it will be the Place.id
    - user_id: string - empty string: it will be the User.id
    - text: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')
