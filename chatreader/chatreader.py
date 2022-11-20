#import asynco
from telethon import TelegramClient
from pickle import load
from datetime import datetime

async def main():
    me = await client.get_me()
    #print(me.stringify())
    
    '''
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    '''
    date_offset = datetime(2022, 9, 20, tzinfo=None)
    async for message in client.iter_messages(-1001776583381, offset_date = date_offset, reverse = True):
        print(message.id, message.text)
if __name__ == '__main__':
    with open('login_conf', 'rb') as f:
        load_conf = load(f)
        f.close()
    # Use your own values from my.telegram.org
    api_id = load_conf['api_id']
    api_hash = load_conf['api_hash']
    username = load_conf['username']
    
    client = TelegramClient(username, api_id, api_hash)
    with client:
        client.loop.run_until_complete(main())