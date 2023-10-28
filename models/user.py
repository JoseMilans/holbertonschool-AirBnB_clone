#!/usr/bin/python3
"""Module for User class"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for the User class"""
    
    def __init__(self, *args, **kwargs):
        """Initializes the User class"""
        super().__init__(*args, **kwargs)
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
