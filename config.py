import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
SIGNING_SECRET = os.getenv('SIGNING_SECRET')
SLACK_TOKEN = os.getenv('SLACK_TOKEN')

# Add additional configuration settings here if needed
