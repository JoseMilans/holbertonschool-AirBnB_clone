#!/usr/bin/python3
"""Module for User class"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
