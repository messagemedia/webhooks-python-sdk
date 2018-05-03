# -*- coding: utf-8 -*-

"""
    message_media_webhooks.controllers.api_controller

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import logging
from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.retrieve_response import RetrieveResponse
from ..exceptions.api_exception import APIException

class APIController(BaseController):

    """A Controller to access Endpoints in the message_media_webhooks API."""

    def __init__(self, client=None, call_back=None):
        super(APIController, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def create(self,
                content_type,
                body):
        """Does a POST request to /v1/webooks/messages.

        This will create a webhook for the specified `events`
        ### Parameters
        **list of supported parameters in `template` according to the message
        type :**
        you must escape the json for the template parameter. see example .
        | Data   | parameter name | DR| MO | MO MMS | Comment |
        |:--|--|--|--|--|--|
        | **service type**  | $type| ``OK`` |`OK`| `OK`| |
        | **Message ID**  | $mtId, $messageId| `OK` |`OK`| `OK`| |
        | **Delivery report ID** |$drId, $reportId | `OK` || | |
        | **Reply ID**| $moId, $replyId| |`OK`| `OK`||
        | **Account ID**  | $accountId| `OK` |`OK`| `OK`||
        | **Message Timestamp**  | $submittedTimestamp| `OK` |`OK`| `OK`||
        | **Provider Timestamp**  | $receivedTimestamp| `OK` |`OK`| `OK`||
        | **Message status** | $status| `OK` ||||
        | **Status code**  | $statusCode| `OK` ||||
        | **External metadata** | $metadata.get('key')| `OK` |`OK`| `OK`||
        | **Source address**| $sourceAddress| `OK` |`OK`| `OK`||
        | **Destination address**| $destinationAddress|  |`OK`| `OK`||
        | **Message content**| $mtContent, $messageContent| `OK` |`OK`|
        `OK`||
        | **Reply Content**| $moContent, $replyContent|  |`OK`| `OK`||
        | **Retry Count**| $retryCount| `OK` |`OK`| `OK`||
        **list of allowed  `events` :**
        you can combine all the events whatever the message type.(at least one
        Event set otherwise the webhook won't be created)
        + **events for SMS**
            + `RECEIVED_SMS`
            + `OPT_OUT_SMS`
        + **events for MMS**
            + `RECEIVED_MMS`
        + **events for DR**
            + `ENROUTE_DR`
            + `EXPIRED_DR`
            + `REJECTED_DR`
            + `FAILED_DR`
            + `DELIVERED_DR`
            + `SUBMITTED_DR`
        a **Response 400 is returned when** :
            <ul>
             <li>the `url` is not valid </li>
             <li>the `events` is null/empty </li>
             <li>the `encoding` is null </li>
             <li>the `method` is null </li>
             <li>the `headers` has a `ContentType`  attribute </li>
            </ul>

        Args:
            content_type (string): TODO: type description here. Example: 
            body (CreateRequest): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/webooks/messages'
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create.')
            _headers = {
                'accept': 'application/json',
                'Content-Type': content_type
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'create')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create.')
            if _context.response.status_code == 400:
                raise APIException('', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def delete_delete_and_update_webhook(self,
                                         webhook_id):
        """Does a DELETE request to /v1/webooks/messages/{webhookId}.

        This will delete the webhook wuth the give id.
        a **Response 404 is returned when** :
            <ul>
             <li>there is no webhook  with this `webhookId` </li>
            </ul>

        Args:
            webhook_id (uuid|string): TODO: type description here. Example: 

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('delete_delete_and_update_webhook called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for delete_delete_and_update_webhook.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/webooks/messages/{webhookId}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'webhookId': webhook_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for delete_delete_and_update_webhook.')
            _request = self.http_client.delete(_query_url)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'delete_delete_and_update_webhook')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for delete_delete_and_update_webhook.')
            if _context.response.status_code == 404:
                raise APIException('', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def retrieve(self,
                 page=None,
                 page_size=None):
        """Does a GET request to /v1/webooks/messages/.

        This will retrieve all webhooks for the account we're connected with.
        a **Response 400 is returned when** :
            <ul>
             <li>the `page` query parameter is not valid </li>
             <li>the `pageSize` query parameter is not valid </li>
            </ul>

        Args:
            page (int, optional): TODO: type description here. Example: 
            page_size (int, optional): TODO: type description here. Example: 

        Returns:
            RetrieveResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('retrieve called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for retrieve.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/webooks/messages/'
            _query_parameters = {
                'page': page,
                'pageSize': page_size
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for retrieve.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for retrieve.')
            _request = self.http_client.get(_query_url, headers=_headers)
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'retrieve')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for retrieve.')
            if _context.response.status_code == 400:
                raise APIException('', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, RetrieveResponse.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update(self,
                webhook_id,
                content_type,
                body):
        """Does a PATCH request to /v1/webooks/messages/{webhookId}.

        This will update a webhook and returned the updated Webhook. 
        you can update all the attributes individually or together.
        PS : the new value will override the previous one.
        ### Parameters
        + same parameters rules as create webhook apply
         a **Response 404 is returned when** :
            <ul>
             <li>there is no webhook with this `webhookId` </li>
            </ul>   
         a **Response 400 is returned when** :
            <ul>
              <li>all attributes are null </li>
             <li>events array is empty </li>
             <li>content-Type is set in the headers instead of using the
             `encoding` attribute  </li>
            </ul>

        Args:
            webhook_id (uuid|string): TODO: type description here. Example: 
            content_type (string): TODO: type description here. Example: 
            body (UpdateRequest): TODO: type description here. Example: 

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for update.')
            _query_builder = Configuration.base_uri
            _query_builder += '/v1/webooks/messages/{webhookId}'
            _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
                'webhookId': webhook_id
            })
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for update.')
            _headers = {
                'Content-Type': content_type
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for update.')
            _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            BasicAuth.apply(_request)
            _context = self.execute_request(_request, name = 'update')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update.')
            if _context.response.status_code == 404:
                raise APIException('', _context)
            self.validate_response(_context)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
