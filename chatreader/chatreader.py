#import asynco
from telethon import TelegramClient
from pickle import load
from datetime import datetime
import mysql.connector
from getpass import getpass

async def main(db_con):
    me = await client.get_me()
    #print(me.stringify())
    
    '''
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)
    '''
    date_offset = datetime(2023, 3, 14, tzinfo=None)
    async for message in client.iter_messages(-1001776583381, offset_date = date_offset, reverse = True):
        #print(message.id, message.text)
        datetime_str=message.date.strftime('%Y-%m-%d %H:%M:%S')
        exist_query = """SELECT id FROM messages_table WHERE id = %s;"""
        with db_con.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (message.id, ))
            result = cursor.fetchall()
            if len(result) == 0:
                insert_mes_query = """INSERT INTO messages_table VALUES (%s, %s, %s);"""
                cursor.execute(insert_mes_query, (message.id, message.text, datetime_str))
                db_con.commit()
            #print(result)

if __name__ == '__main__':
    try:
        with mysql.connector.connect(host="localhost",
                                     user=input("Имя пользователя: "),
                                     password=getpass("Пароль: "),
                                     database="pograncontrol"
                                     ) as connection:
            print(connection)
            with open('login_conf', 'rb') as f:
                load_conf = load(f)
                f.close()
            # Use your own values from my.telegram.org
            api_id = load_conf['api_id']
            api_hash = load_conf['api_hash']
            username = load_conf['username']
            
            client = TelegramClient(username, api_id, api_hash)
            with client:
                client.loop.run_until_complete(main(connection))
    except mysql.connector.Error as e:
        print(e)
            
