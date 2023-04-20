import mysql.connector
from getpass import getpass
def read_db_messages_table(db_con):
    exist_query = """SELECT * FROM messages_table;"""
    with db_con.cursor(buffered = True) as cursor:
        cursor.execute(exist_query)
        res = cursor.fetchall()
    for i in res:
        text=i[1].replace("'", "")
        with db_con.cursor(buffered = True) as cursor:
            insert_mes_query = """UPDATE messages_table SET text = %s WHERE id = (%s);"""
            cursor.execute(insert_mes_query, (text, i[0]))
            db_con.commit()

with mysql.connector.connect(host="localhost",
                             user=input("Имя пользователя: "),
                             password=getpass("Пароль: "),
                             database="pograncontrol"
                             ) as connection:
    read_db_messages_table(connection)
