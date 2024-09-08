import os
import asyncio
import logging
from flask import Flask, request, Response
from dotenv import load_dotenv
from slack_sdk.errors import SlackApiError
from slack_sdk.web.async_client import AsyncWebClient
from slackeventsapi import SlackEventAdapter

from events import handle_message_event, handle_reaction_event
from models import init_db, get_message_count

# Load environment variables
load_dotenv()

# Setup Flask app and Slack event adapter
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.getenv('SIGNING_SECRET'), '/slack/events', app)

# Async Slack WebClient
client = AsyncWebClient(token=os.getenv('SLACK_TOKEN'))
BOT_ID = None

# Logging setup
logging.basicConfig(level=logging.INFO)

# Initialize the database
init_db()


# Slack Event Handlers
@slack_event_adapter.on('message')
async def handle_message(payload):
    """Handles incoming messages from Slack."""
    event = payload.get('event', {})
    await handle_message_event(event, client, BOT_ID)


@slack_event_adapter.on('reaction_added')
async def handle_reaction(payload):
    """Handles reaction added events."""
    event = payload.get('event', {})
    await handle_reaction_event(event, client)


@app.route('/message-count', methods=['POST'])
async def message_count():
    """Returns the message count for a user."""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    count = get_message_count(user_id)

    try:
        await client.chat_postMessage(channel=channel_id, text=f"Message count: {count}")
    except SlackApiError as e:
        logging.error(f"Error posting message count: {e.response['error']}")
    return Response(), 200


# Initialize Slack Bot ID and start Flask app
if __name__ == "__main__":
    BOT_ID = asyncio.run(client.auth_test())['user_id']
    app.run(debug=True)
