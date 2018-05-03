# -*- coding: utf-8 -*-

"""
    message_media_webhooks.models.update_request_15

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class UpdateRequest15(object):

    """Implementation of the 'Update request15' model.

    TODO: type model description here.

    Attributes:
        url (string): target for the webhook. http and https are authorized
        template (string): expected template. see doc for possibilitie

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "template":'template'
    }

    def __init__(self,
                 url=None,
                 template=None):
        """Constructor for the UpdateRequest15 class"""

        # Initialize members of the class
        self.url = url
        self.template = template


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
        url = dictionary.get('url')
        template = dictionary.get('template')

        # Return an object of this model
        return cls(url,
                   template)


