#!/usr/bin/python3
"""
Module containing the State class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class with a name attribute.

    Public class attributes:
    - name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the State class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
