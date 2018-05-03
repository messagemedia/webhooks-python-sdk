# -*- coding: utf-8 -*-

"""
    message_media_webhooks.models.update_request

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io )
"""


class UpdateRequest(object):

    """Implementation of the 'Update request' model.

    TODO: type model description here.

    Attributes:
        url (string): target for the webhook. http and https are authorized
        method (string): authorized webhook methods  :  GET, POST, PUT,
            DELETE, PATCH
        encoding (string): JSON, FORM_ENCODED, XML
        headers (object): customized headers.no content Type header because we
            set it in the encoding attribute. an example belowf
        events (list of string): list of events we want to suscribe to. see
            docs
        template (string): expected template. see doc for possibilitie

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url":'url',
        "method":'method',
        "encoding":'encoding',
        "headers":'headers',
        "events":'events',
        "template":'template'
    }

    def __init__(self,
                 url=None,
                 method=None,
                 encoding=None,
                 headers=None,
                 events=None,
                 template=None):
        """Constructor for the UpdateRequest class"""

        # Initialize members of the class
        self.url = url
        self.method = method
        self.encoding = encoding
        self.headers = headers
        self.events = events
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
        method = dictionary.get('method')
        encoding = dictionary.get('encoding')
        headers = dictionary.get('headers')
        events = dictionary.get('events')
        template = dictionary.get('template')

        # Return an object of this model
        return cls(url,
                   method,
                   encoding,
                   headers,
                   events,
                   template)


