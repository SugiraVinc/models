#!/usr/bin/python3
from base_model import BaseModel


class User(BaseModel):
    """ a class for user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
