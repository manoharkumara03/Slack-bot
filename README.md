# Slack Bot Application

This project is a Slack bot built using Flask and the Slack API. It interacts with users, sends scheduled messages, monitors for bad words, and handles reactions. The bot can also track and report message counts.

## Features

- **Welcome Messages**: Sends a welcome message to new users who type "start".
- **Scheduled Messages**: Allows scheduling messages to be sent at a future time.
- **Bad Words Filtering**: Detects and responds to messages containing predefined bad words.
- **Message Count Tracking**: Tracks the number of messages sent by each user.
- **Reaction Handling**: Updates messages when users react with a specific emoji.

## Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/slack-bot.git
    cd slack-bot
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    Create a `.env` file in the root of the project with the following content:

    ```env
    # Slack API credentials
    SLACK_TOKEN=your-slack-bot-token-here
    SIGNING_SECRET=your-slack-signing-secret-here

    # Optional: Add additional configuration if needed
    ```

5. **Run the Application**

    ```bash
    python app.py
    ```

## Configuration

- **SLACK_TOKEN**: Your Slack bot token. Get it from the Slack API dashboard.
- **SIGNING_SECRET**: Your Slack app's signing secret for request verification.

## Usage

- **Start the Bot**: Run the application as described above.
- **Send a "start" Message**: Type "start" in any channel where the bot is present to receive a welcome message.
- **React to Welcome Messages**: React to the welcome message to mark it as complete.
- **Message Count**: Send a POST request to `/message-count` with `user_id` and `channel_id` to get the message count for a user.

### Example POST Request for Message Count

```bash
curl -X POST http://localhost:5000/message-count \
    -d "user_id=U12345678" \
    -d "channel_id=C12345678"
```

## Development

- **Database**: Uses SQLite for message count tracking. Initialize with `models.py`.
- **Logging**: Logs errors and important information to the console.

## Contributing

Feel free to open issues or submit pull requests if you have improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
- Replace placeholders like `your-slack-bot-token-here` and `your-slack-signing-secret-here` with actual values.
- Adjust any instructions or sections according to specific needs or changes in the project.
