# -*- coding: utf-8 -*-

"""
    message_media_webhooks.models.headers

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class Headers(object):

    """Implementation of the 'headers' model.

    TODO: type model description here.

    Attributes:
        account (string): Example of

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account":'Account'
    }

    def __init__(self,
                 account=None):
        """Constructor for the Headers class"""

        # Initialize members of the class
        self.account = account


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        account = dictionary.get('Account')

        # Return an object of this model
        return cls(account)


