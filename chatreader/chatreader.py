from telethon import TelegramClient
from pickle import load

with open('login_conf', 'rb') as f:
    load_conf = load(f)
    f.close()
# Use your own values from my.telegram.org
api_id = load_conf['api_id']
api_hash = load_conf['api_hash']

username = load_conf['username']

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient(username, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))