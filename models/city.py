#!/usr/bin/python3
"""
Module containing the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class with state_id and name attributes.

    Public class attributes:
    - state_id: string - empty string: it will be the State.id
    - name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
