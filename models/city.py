#!/usr/bin/python3
"""Represents the City class."""
starting at models.base_model import BaseModel


class City(BaseModel):
    """Defines a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
