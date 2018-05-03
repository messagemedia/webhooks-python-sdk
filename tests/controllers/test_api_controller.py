# -*- coding: utf-8 -*-

"""
    tests.controllers.test_api_controller

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from message_media_webhooks.api_helper import APIHelper


class APIControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(APIControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.client

    # This will delete the webhook wuth the give id.
    #a **Response 404 is returned when** :
    #    <ul>
    #     <li>there is no webhook  with this `webhookId` </li>
    #    </ul>
    def test_delete_delete_and_update_webhook_1(self):
        # Parameters for the API call
        webhook_id = 'a7f11bb0-f299-4861-a5ca-9b29d04bc5ad'

        # Perform the API call through the SDK function
        self.controller.delete_delete_and_update_webhook(webhook_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = None

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # This will retrieve all webhooks for the account we're connected with.
    #a **Response 400 is returned when** :
    #    <ul>
    #     <li>the `page` query parameter is not valid </li>
    #     <li>the `pageSize` query parameter is not valid </li>
    #    </ul>
    def test_retrieve_1(self):
        # Parameters for the API call
        page = '1'
        page_size = '10'

        # Perform the API call through the SDK function
        result = self.controller.retrieve(page, page_size)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = None

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize((
            '{"page":0,"pageSize":100,"pageData":[{"id":"6e2c61df-d30a-4555-82a5-0e79822'
            'd8f53","url":"http://myurl.com","method":"POST","encoding":"FORM_ENCODED","'
            'headers":{"Account":"FunGuys"},"template":"id=$mtId&status=$statusCode","ev'
            'ents":["ENROUTE_DR","DELIVERED_DR"]},{"id":"6e2c61df-d30a-4555-82a5-0e79822'
            'd8f53","url":"http://myurl.com","method":"POST","encoding":"XML","headers":'
            '{"Account":"FunGuys"},"template":"<content><id> $mtId < /id> <status > $sta'
            'tusCode < /status> </content>","events":["ENROUTE_DR","DELIVERED_DR"]}]}'
            ))
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body, check_values = True))


