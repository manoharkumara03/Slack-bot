import logging
from utils import check_if_bad_words, send_welcome_message, update_reaction_status
from models import increment_message_count

BAD_WORDS = ['hmm', 'no', 'tim']

async def handle_message_event(event, client, bot_id):
    """Processes the message event from Slack."""
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if user_id and bot_id != user_id:
        # Increment message count in the database
        increment_message_count(user_id)

        # Send welcome message if user types 'start'
        if text.lower() == 'start':
            await send_welcome_message(channel_id, user_id, client)

        # Check for bad words
        elif check_if_bad_words(text, BAD_WORDS):
            ts = event.get('ts')
            try:
                await client.chat_postMessage(
                    channel=channel_id, thread_ts=ts, text="Please avoid using inappropriate words!")
            except SlackApiError as e:
                logging.error(f"Error posting bad word warning: {e.response['error']}")


async def handle_reaction_event(event, client):
    """Processes the reaction added event from Slack."""
    user_id = event.get('user')
    channel_id = event.get('item', {}).get('channel')

    # Update the welcome message reaction status
    await update_reaction_status(user_id, channel_id, client)
  
