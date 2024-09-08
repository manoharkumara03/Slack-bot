import sqlite3

def init_db():
    """Initializes the database."""
    conn = sqlite3.connect('slack_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS message_count (
            user_id TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def increment_message_count(user_id):
    """Increments the message count for a user."""
    conn = sqlite3.connect('slack_bot.db')
    cursor = conn.cursor()

    cursor.execute('SELECT count FROM message_count WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()

    if row:
        cursor.execute('UPDATE message_count SET count = count + 1 WHERE user_id = ?', (user_id,))
    else:
        cursor.execute('INSERT INTO message_count (user_id, count) VALUES (?, 1)', (user_id,))

    conn.commit()
    conn.close()


def get_message_count(user_id):
    """Retrieves the message count for a user."""
    conn = sqlite3.connect('slack_bot.db')
    cursor = conn.cursor()

    cursor.execute('SELECT count FROM message_count WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()

    conn.close()
    return row[0] if row else 0
  
