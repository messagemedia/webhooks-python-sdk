from message_media_webhooks.message_media_webhooks_client import MessageMediaWebhooksClient
from message_media_webhooks.models.create_webhook_request import CreateWebhookRequest

basic_auth_user_name = 'API_KEY' # The username to use with basic authentication
basic_auth_password = 'API_SECRET' # The password to use with basic authentication

client = MessageMediaWebhooksClient(basic_auth_user_name, basic_auth_password)
webhooks_controller = client.webhooks

webhook_id = "WEBHOOK_ID"

webhooks_controller.delete_webhook(webhook_id)
