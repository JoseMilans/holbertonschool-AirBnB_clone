#!/usr/bin/python3
"""Initialises and sets up the storage process"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
