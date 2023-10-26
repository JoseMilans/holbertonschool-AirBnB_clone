#!/usr/bin/python3
"""Initialises and sets up the storage process"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
