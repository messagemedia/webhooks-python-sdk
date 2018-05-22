# MessageMedia Webhooks Python SDK
[![Travis Build Status](https://api.travis-ci.org/messagemedia/webhooks-python-sdk.svg?branch=master)](https://travis-ci.org/messagemedia/webhooks-python-sdk)
[![PyPI](https://badge.fury.io/py/messagemedia-webhooks-sdk.svg)](https://pypi.python.org/pypi/messagemedia-webhooks-sdk)

The MessageMedia Webhooks allows you to subscribe to one or several events and when one of those events is triggered, an HTTP request is sent to the URL of your choice along with the message or payload. In simpler terms, it allows applications to "speak" to one another and get notified automatically when something new happens.

## ⭐️ Install via PIP
Run the following command to install the SDK via pip:
`pip install messagemedia-webhooks-sdk`

## 🎬 Get Started
It's easy to get started. Simply enter the API Key and secret you obtained from the [MessageMedia Developers Portal](https://developers.messagemedia.com) into the code snippet below and a mobile number you wish to send to.

### 🚀 Create a webhook
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

### 📥 Retrieve all webhooks
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

### 🔄 Update a webhook
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

### ❌ Delete a webhook
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

## 📕 Documentation
Check out the [full API documentation](DOCUMENTATION.md) for more detailed information.

## 😕 Need help?
Please contact developer support at developers@messagemedia.com or check out the developer portal at [developers.messagemedia.com](https://developers.messagemedia.com/)

## 📃 License
Apache License. See the [LICENSE](LICENSE) file.
