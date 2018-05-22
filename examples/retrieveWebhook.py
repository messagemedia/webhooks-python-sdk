from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
from message_media_webhooks.models.create_webhook_request import CreateWebhookRequest

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

page = 0
page_size = 0

result = webhooks_controller.retrieve_webhook(page, page_size)
