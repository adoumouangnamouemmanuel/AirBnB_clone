#!usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user

    Attributes:
        email
        password
        first_name
        last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
