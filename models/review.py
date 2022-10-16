#!/usr/bin/python3
"""
contains the Review class

"""


from models.base_model import BaseModel


class Review(BaseModel):

    """

    Review has the following attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string

    """
    place_id = ""
    user_id = ""
    text = ""
