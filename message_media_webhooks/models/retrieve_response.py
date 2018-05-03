# -*- coding: utf-8 -*-

"""
    message_media_webhooks.models.retrieve_response

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class RetrieveResponse(object):

    """Implementation of the 'Retrieve response' model.

    TODO: type model description here.

    Attributes:
        page (int): TODO: type description here.
        page_size (int): TODO: type description here.
        page_data (list of object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page":'page',
        "page_size":'pageSize',
        "page_data":'pageData'
    }

    def __init__(self,
                 page=None,
                 page_size=None,
                 page_data=None):
        """Constructor for the RetrieveResponse class"""

        # Initialize members of the class
        self.page = page
        self.page_size = page_size
        self.page_data = page_data


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
        page = dictionary.get('page')
        page_size = dictionary.get('pageSize')
        page_data = dictionary.get('pageData')

        # Return an object of this model
        return cls(page,
                   page_size,
                   page_data)


