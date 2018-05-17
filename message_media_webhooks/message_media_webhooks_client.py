# -*- coding: utf-8 -*-

"""
    message_media_webhooks.message_media_webhooks_client

    
"""
from .decorators import lazy_property
from .configuration import Configuration
from .controllers.api_controller import APIController

class MessageMediaWebhooksClient(object):

    config = Configuration

    @lazy_property
    def client(self):
        return APIController()


    def __init__(self, 
                 basic_auth_user_name = None,
                 basic_auth_password = None):
        if basic_auth_user_name != None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password != None:
            Configuration.basic_auth_password = basic_auth_password


