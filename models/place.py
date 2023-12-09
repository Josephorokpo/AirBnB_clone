#!/usr/bin/python3
"""
Module containing the Place class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class with city_id, user_id, name, description, number_rooms,
    number_bathrooms, max_guest, price_by_night, latitude, longitude,
    and amenity_ids attributes.

    Public class attributes:
    - city_id: string - empty string: it will be the City.id
    - user_id: string - empty string: it will be the User.id
    - name: string - empty string
    - description: string - empty string
    - number_rooms: integer - 0
    - number_bathrooms: integer - 0
    - max_guest: integer - 0
    - price_by_night: integer - 0
    - latitude: float - 0.0
    - longitude: float - 0.0
    - amenity_ids: list of string - empty list: it will be the
    list of Amenity.id later
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Place class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])
