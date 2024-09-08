import logging
from slack_sdk.errors import SlackApiError

def check_if_bad_words(message, bad_words):
    """Check if a message contains any bad words."""
    message_clean = message.lower().translate(str.maketrans('', '', string.punctuation))
    return any(word in message_clean for word in bad_words)


async def send_welcome_message(channel, user, client):
    """Sends a welcome message to the user."""
    welcome_message = {
        'channel': channel,
        'text': 'Welcome to this awesome channel! Please follow the guidelines.',
        'username': 'Welcome Bot',
        'icon_emoji': ':robot_face:'
    }
    
    try:
        await client.chat_postMessage(**welcome_message)
    except SlackApiError as e:
        logging.error(f"Error sending welcome message: {e.response['error']}")


async def update_reaction_status(user_id, channel_id, client):
    """Updates the welcome message status after a reaction."""
    try:
        # Simulated logic for updating a message (you can expand this logic)
        await client.chat_postMessage(
            channel=channel_id, text=f"Thank you, <@{user_id}> for reacting!")
    except SlackApiError as e:
        logging.error(f"Error updating reaction status: {e.response['error']}")
      
