#!/usr/bin/python3
"""__init__ module is to initialize the package models
   it defines specific FileStorage instance storage for the importing module
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
