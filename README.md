# MessageMedia Webhooks Python SDK
[![Travis Build Status](https://api.travis-ci.org/messagemedia/webhooks-python-sdk.svg?branch=master)](https://travis-ci.org/messagemedia/webhooks-python-sdk)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![PyPI](https://badge.fury.io/py/messagemedia-webhooks-sdk.svg)](https://pypi.python.org/pypi/messagemedia-webhooks-sdk)

The MessageMedia Webhooks allows you to subscribe to one or several events and when one of those events is triggered, an HTTP request is sent to the URL of your choice along with the message or payload. In simpler terms, it allows applications to "speak" to one another and get notified automatically when something new happens.

![Webhooks Flow](http://i66.tinypic.com/2ufxf81.jpg)

## Table of Contents
* [Authentication](#closed_lock_with_key-authentication)
* [Errors](#interrobang-errors)
* [Information](#newspaper-information)
  * [Slack and Mailing List](#slack-and-mailing-list)
  * [Bug Reports](#bug-reports)
  * [Contributing](#contributing)
* [Installation](#star-installation)
* [Get Started](#clapper-get-started)
* [API Documentation](#closed_book-api-documentation)
* [Need help?](#confused-need-help)
* [License](#page_with_curl-license)

## :closed_lock_with_key: Authentication

Authentication is done via API keys. Sign up at https://developers.messagemedia.com/register/ to get your API keys.

Requests are authenticated using HTTP Basic Auth or HMAC. Provide your API key as the auth_user_name and API secret as the auth_password.

## :interrobang: Errors

Our API returns standard HTTP success or error status codes. For errors, we will also include extra information about what went wrong encoded in the response as JSON. The most common status codes are listed below.

#### HTTP Status Codes

| Code      | Title       | Description |
|-----------|-------------|-------------|
| 400 | Invalid Request | The request was invalid |
| 401 | Unauthorized | Your API credentials are invalid |
| 403 | Disabled feature | Feature not enabled |
| 404 | Not Found |	The resource does not exist |
| 50X | Internal Server Error | An error occurred with our API |

## :newspaper: Information

#### Slack and Mailing List

If you have any questions, comments, or concerns, please join our Slack channel:
https://developers.messagemedia.com/collaborate/slack/

Alternatively you can email us at:
developers@messagemedia.com

#### Bug reports

If you discover a problem with the SDK, we would like to know about it. You can raise an [issue](https://github.com/messagemedia/signingkeys-nodejs-sdk/issues) or send an email to: developers@messagemedia.com

#### Contributing

We welcome your thoughts on how we could best provide you with SDKs that would simplify how you consume our services in your application. You can fork and create pull requests for any features you would like to see or raise an [issue](https://github.com/messagemedia/signingkeys-nodejs-sdk/issues)

## :star: Installation
Run the following command to install the SDK via pip:
```
pip install messagemedia-webhooks-sdk
```

## :clapper: Get Started
It's easy to get started. Simply enter the API Key and secret you obtained from the [MessageMedia Developers Portal](https://developers.messagemedia.com) into the code snippet below.

### Create a webhook
```python
from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
from message_media_webhooks.models.create_webhook_request import CreateWebhookRequest

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

body = CreateWebhookRequest("http://webhook.com", "POST", "JSON", None, ["ENROUTE_DR"], "{\"id\":\"$mtId\",\"status\":\"$statusCode\"}")

result = webhooks_controller.create_webhook(body)

```

### Retrieve all webhooks
```python
from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
from message_media_webhooks.models.create_webhook_request import CreateWebhookRequest

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

page = 0
page_size = 0

result = webhooks_controller.retrieve_webhook(page, page_size)

```

### Update a webhook
You can get a webhook ID by looking at the `id` of each webhook created from the response of the above example.
```python
from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
import json

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

webhook_id = "WEBHOOK_ID"
body_value = "{\"url\": \"https://myurl.com\",\"method\": \"POST\", \"encoding\": \"FORM_ENCODED\", \"events\": [\"ENROUTE_DR\"],\"template\": \"{\\\"id\\\":\\\"$mtId\\\", \\\"status\\\":\\\"$statusCode\\\"}\" }"

body = json.loads(body_value)

result = webhooks_controller.update_webhook(webhook_id, body)

```

### Delete a webhook
You can get a webhook ID by looking at the `id` of each webhook created from the response of the retrieve webhooks example.
```python
from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
from message_media_webhooks.models.create_webhook_request import CreateWebhookRequest

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

body = CreateWebhookRequest("http://webhook.com", "POST", "JSON", None, ["ENROUTE_DR"], "{\"id\":\"$mtId\",\"status\":\"$statusCode\"}")

result = webhooks_controller.create_webhook(body)

```

## :closed_book: API Reference Documentation
Check out the [full API documentation](https://developers.messagemedia.com/code/webhooks-api-documentation/) for more detailed information.

## :confused: Need help?
Please contact developer support at developers@messagemedia.com or check out the developer portal at [developers.messagemedia.com](https://developers.messagemedia.com/)

## :page_with_curl: License
Apache License. See the [LICENSE](LICENSE) file.
