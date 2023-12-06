#!/usr/bin/python3
"""
Initialize and reload the storage for the application.
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
