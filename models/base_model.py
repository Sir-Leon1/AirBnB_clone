#!/usr/bin/python3
"""Defines the baseModel class."""
import models
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """Rep the base model of the hbnh project"""


    def __init__(self, *args, **kwargs):
        """Initialize a new basemodel."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.create_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v

        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
