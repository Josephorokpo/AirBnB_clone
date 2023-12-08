#!/usr/bin/python3
"""
Module containing the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class with email, password, first_name, and last_name attributes.

    Public class attributes:
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the User class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
