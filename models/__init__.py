"""__init__ magic method for models directory"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
