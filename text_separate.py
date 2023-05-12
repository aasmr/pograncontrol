import mysql.connector
from pograncontrol.separate_ui import *
from getpass import getpass
from datetime import datetime

class Signals(QObject):
    mesDateSignal = Signal(str, str)
    mesTxtSignal = Signal(str)
    def __init__(self):
        super().__init__()

class PogranControl():
    def __init__(self, mes_text, mes_id, mes_date):
        self.mes_text = mes_text
        self.mes_id = mes_id
        self.mes_count = 0
        self.mes_date=mes_date
        
    def initUI(self):
        self.sg = Signals()
        self.uiWorker = ui(self)
        self.uiWorker.sg.endInitSignal.connect(self.startWorker)
        self.uiWorker.exitBut.clicked.connect(self.exit) 
        self.uiWorker.writeBut.clicked.connect(self.writecase)
        self.uiWorker.passBut.clicked.connect(self.passText)
        self.uiWorker.sg.writeSignal.connect(self.separateText)
        self.uiWorker.sg.endInitSignal.emit()
        #self.uiWorker.contBut.clicked.connect(self.startWorker)
        
        
    def startWorker(self):
        while check_db_case_text(db_con, self.mes_id[self.mes_count]) == True or check_db_messages_info(db_con, self.mes_id[self.mes_count]) == True :
            self.mes_count +=1
            
        mesTextforUI = self.mes_text[self.mes_count]
        mesDate = self.mes_date[self.mes_count].strftime('%Y-%m-%d %H:%M:%S')
        self.sg.mesTxtSignal.emit(mesTextforUI)
        msgCnt=str(self.mes_count) + '/' + str(len(self.mes_text))
        self.sg.mesDateSignal.emit(msgCnt, mesDate)
    
    def passText(self):
        write_db_messages_info(db_con, self.mes_id[self.mes_count], "pass")
        self.mes_count+=1
        self.startWorker()
    @Slot(str, str)
    def separateText(self, sep, date):
        if date == '':
            date = None
        else:
            try:
                dt_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') 
            except:
                dt_date = datetime.strptime(date, '%Y-%m-%d')   
        ls = self.mes_text[self.mes_count].split(sep)
        print(ls)
        for i in ls:
            if not ('Канал опытного переезжальщика - @kyrillic' in i) and not ('Как построить жизнь, карьеру и бизнес за рубежом: @berkovskaya_elena' in i):
                write_db_case_text(db_con, self.mes_id[self.mes_count], i, dt_date)
        self.mes_count+=1
        self.startWorker()    
        
    def writecase(self):
        write_db_case_text(db_con, self.mes_id[self.mes_count], self.mes_text[self.mes_count], self.mes_date[self.mes_count])       
        self.mes_count+=1
        self.startWorker()
          
    def exit(self):        
        self.uiWorker.close()
        db_con.close()

def db_connect():
    return mysql.connector.connect(host="localhost",
                                     user=input("Имя пользователя: "),
                                     password=getpass("Пароль: "),
                                     database="pograncontrol"
                                     )
    
def read_db_messages_table(db_con):
    exist_query = """SELECT * FROM messages_table;"""
    with db_con.cursor(buffered = True) as cursor:
        cursor.execute(exist_query)
        res = cursor.fetchall()
    msg_id = []
    msg_txt = []
    msg_date = []
    for i in res:
        msg_id.append(i[0])
        msg_txt.append(i[1])
        msg_date.append(i[2])

    return msg_id, msg_txt, msg_date

def check_db_case_text(db_con, msg_id):
        exist_query = """SELECT msg_id FROM case_text WHERE msg_id = %s;"""
        with db_con.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (msg_id,))
            result = cursor.fetchall()
            if len(result) == 0:
                return False
            else:
                return True
def check_db_messages_info(db_con, msg_id):
        exist_query = """SELECT tag FROM messages_info WHERE msg_id = %s;"""
        with db_con.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (msg_id,))
            result = cursor.fetchone()
            if result == None:
                return False
            elif len(result) == 0:
                return False
            elif result[0] == 'pass':
                return True
            else:
                return False
def write_db_case_text(db_con, msg_id, txt, date):
        with db_con.cursor(buffered = True) as cursor:
            insert_mes_query = """INSERT INTO case_text (msg_id, date, text) VALUES (%s, %s, %s);"""
            cursor.execute(insert_mes_query, (msg_id, date, txt))
            db_con.commit()

def write_db_messages_info(db_con, msg_id, tag):
        with db_con.cursor(buffered = True) as cursor:
            insert_mes_query = """INSERT INTO messages_info (msg_id, tag, author) VALUES (%s, %s, %s);"""
            cursor.execute(insert_mes_query, (msg_id, tag, "aasmr"))
            db_con.commit()         
            
if __name__ == '__main__':
    app = QApplication([])
    db_con = db_connect()
    res = read_db_messages_table(db_con)
    pogranworker=PogranControl(res[1], res[0], res[2])
    pogranworker.initUI()
    pogranworker.uiWorker.show()
    #pogranworker.startWorker()
    sys.exit(app.exec_())
        
    