'''
Created on 28 окт. 2022 г.

@author: aasmr
'''
import mysql.connector
from getpass import getpass
import json
import logging
import os.path
import pandas as pd
import csv
import sys
import numpy as np
from pograncontrol.pogran_ui import *
from datetime import datetime

# для отлавливания ошибок
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))
    print(text)
    #QtWidgets.QMessageBox.critical(None, 'Error', text)
    # quit()            
        
sys.excepthook = log_uncaught_exceptions 

class Signals(QObject):
    mesTxtSignal = Signal(str)
    mesTxtFullSignal = Signal(str)
    mesDateSignal = Signal(str, str)
    mesSetCompleter = Signal(list, list, list, list, list, list, list, list, list, list, list, list)
    mesAutoFill = Signal(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
    mesStatus = Signal(str)
    def __init__(self):
        super().__init__()

class PogranControl():
    def __init__(self, case_type =[], sex =[], age = [], cause = [], army_relations = [], vus = [],
                 army_type = [], army_sec_type = [], army_other = [], country = [], kpp = [],
                 yService = [], voenk_region = [], voenk_city = [], voenk_district = [],
                 kategory = [], katZ = [], date = [], id_ls = [], case_id = []):


        self.case_type = case_type
        self.sex = sex
        self.age = age
        self.cause = cause
        self.army_relations = army_relations
        self.vus = vus
        self.army_type = army_type
        self.army_sec_type = army_sec_type
        self.army_other = army_other
        self.country = country
        self.kpp = kpp
        self.yService = yService
        self.voenk_region = voenk_region
        self.voenk_city = voenk_city
        self.voenk_district = voenk_district
        self.kategory = kategory
        self.katZ = katZ
        self.date = date
        self.id = id_ls
        self.case_id = case_id
        
        self.mes_count=0
        
    def initChatLists(self, mes, chat_id, chat_tag, chat_mID, d_f_mes, d_dtime):
        self.chat_mes = mes
        self.chat_id = chat_id
        self.chat_tag = chat_tag
        self.chat_mID = chat_mID
        
        self.dct_fullmes = d_f_mes
        self.dct_dtime = d_dtime

        
    
    def initUI(self):
        
        self.sg = Signals()
        self.uiWorker = ui(self)
        self.uiWorker.sg.endInitSignal.connect(self.startWorker)
        self.uiWorker.sg.writeSignal.connect(self.writecase)
        self.uiWorker.sg.addSignal.connect(self.addCase)
        self.uiWorker.exitBut.clicked.connect(self.exit) 
        self.uiWorker.contBut.clicked.connect(self.contWrite)
        self.uiWorker.vbrosBut.clicked.connect(self.writeVbros)
        self.uiWorker.dltBut.clicked.connect(self.deleteRow)
        self.uiWorker.showBut.clicked.connect(self.showFullMes)
        
        self.uiWorker.sg.endInitSignal.emit()
        #self.uiWorker.contBut.clicked.connect(self.startWorker)
        
    def startWorker(self):
        self.sg.mesStatus.emit('')
        try:
            self.cause_unq = np.unique(self.cause).tolist()
        except:
            self.cause_unq = []
        try:
            self.army_relations_unq = np.unique(self.army_relations).tolist()
        except:
            self.army_relations_unq = []
        try:
            self.vus_unq = np.unique(self.vus).tolist()
        except:
            self.vus_unq = []
        try:
            self.army_type_unq = np.unique(self.army_type).tolist()
        except:
            self.army_type_unq = []
        try:
            self.army_sec_type_unq = np.unique(self.army_sec_type).tolist()
        except:
            self.army_sec_type_unq = []
        try:
            self.army_other_unq = np.unique(self.army_other).tolist()
        except:
            self.army_other_unq = []
        try:
            self.country_unq = np.unique(self.country).tolist()
        except:
            self.country_unq = []
        try:
            self.kpp_unq = np.unique(self.kpp).tolist()
        except:
            self.kpp_unq = []
        try:
            self.yService_unq = np.unique(self.yService).tolist()
        except:
            self.yService_unq = []
        try:
            self.voenk_region_unq = np.unique(self.voenk_region).tolist()
        except:
            self.voenk_region_unq = []
        try:
            self.voenk_city_unq = np.unique(self.voenk_city).tolist()
        except:
            self.voenk_city_unq = []
        try:
            self.voenk_district_unq = np.unique(self.voenk_district).tolist()
        except:
            self.voenk_district_unq = []
            
        self.sg.mesSetCompleter.emit(self.cause_unq, self.army_relations_unq,
                                     self.vus_unq, self.army_type_unq,
                                     self.army_sec_type_unq, self.army_other_unq,
                                     self.country_unq, self.kpp_unq,
                                     self.yService_unq, self.voenk_region_unq,
                                     self.voenk_city_unq, self.voenk_district_unq)

        if self.mes_count < len(self.chat_mes):
            while check_db_case_text(conn, self.chat_id[self.mes_count]) == True:
                self.mes_count +=1
            mesTextforUI =  self.chat_mes[self.mes_count]
            msgCnt=str(self.mes_count+1) + '/' + str(len(self.chat_mes))
            self.sg.mesTxtSignal.emit(mesTextforUI)
            self.sg.mesDateSignal.emit(self.dct_dtime[self.mes_count].strftime('%Y-%m-%d %H:%M:%S'), msgCnt)

    @Slot(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
    def writecase(self, case_type, sex, age, cause, army_relations, vus, army_type,
                  army_sec_type, army_other, country, kpp, yService, voenk_region,
                  voenk_city, voenk_district, kategory, katZ, date):
        
        if case_type == '':
            self.sg.mesStatus.emit('Тип случая не может быть пустым')
            return
        
        self.case_type.append(case_type)
        self.sex.append(sex)
        self.age.append(age)
        self.cause.append(cause)
        self.army_relations.append(army_relations)
        self.vus.append(vus)
        self.army_type.append(army_type)
        self.army_sec_type.append(army_sec_type)
        self.army_other.append(army_other)
        self.country.append(country)
        self.kpp.append(kpp)
        self.yService.append(yService)
        self.voenk_region.append(voenk_region)
        self.voenk_city.append(voenk_city)
        self.voenk_district.append(voenk_district)
        self.kategory.append(kategory)
        self.katZ.append(katZ)
        self.date.append(date[:10])
        self.id.append(self.chat_mID[self.mes_count])
        

        if sex == '':
            sex = None
        if age == '':
            age = None
        if cause == '':
            cause = None
        if army_relations == '':
            army_relations = None
        if vus == '':
            vus = None
        if army_type == '':
            army_type = None
        if army_sec_type == '':
            army_sec_type = None
        if army_other == '':
            army_other = None
        if country == '':
            country = None
        if kpp == '':
            kpp = None
        if yService == '':
            yService = None
        if voenk_region == '':
            voenk_region = None
        if voenk_city == '':
            voenk_city = None
        if voenk_district == '':
            voenk_district = None
        if kategory == '':
            kategory = None
        if katZ == '':
            katZ = None
        if date == '':
            date = None
        else:
            try:
                dt_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') 
            except:
                dt_date = datetime.strptime(date, '%Y-%m-%d')        
        
        exist_query = """SELECT id FROM pograncontrol.`case` where msg_id = %s AND age = %s AND cause = %s"""
        with conn.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (self.chat_mID[self.mes_count], age, cause))
            result = cursor.fetchall()
        if len(result) > 1:
            self.sg.mesStatus.emit('Введите данные вручную')
        elif len(result) > 0:
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE pograncontrol.`case` SET msg_id = %s, case_mes_id = %s, case_type = %s, age = %s, sex = %s, cause = %s, army_relations = %s, vus = %s, army_type = %s, army_sec_type = %s, army_other = %s, country = %s, kpp = %s, yService = %s, voenk_region = %s, voenk_city = %s, voenk_district = %s, kategory_h = %s, kategory_z = %s, date = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, (self.chat_mID[self.mes_count],
                                                  self.chat_id[self.mes_count],
                                                  case_type, age, sex, cause,
                                                  army_relations, vus, army_type,
                                                  army_sec_type, army_other,
                                                  country, kpp, yService,
                                                  voenk_region, voenk_city,
                                                  voenk_district, kategory, katZ,
                                                  dt_date, result[0]))
                conn.commit()
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, ('marked', 'aasmr', self.chat_id[self.mes_count]))
                conn.commit()
        else:
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """INSERT INTO pograncontrol.`case` (msg_id, case_mes_id, case_type, age, sex, cause, army_relations, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_region, voenk_city, voenk_district, kategory_h, kategory_z, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(insert_mes_query, (self.chat_mID[self.mes_count],
                                                  self.chat_id[self.mes_count],
                                                  case_type, age, sex, cause,
                                                  army_relations, vus, army_type,
                                                  army_sec_type, army_other,
                                                  country, kpp, yService,
                                                  voenk_region, voenk_city,
                                                  voenk_district, kategory, katZ,
                                                  dt_date))
                conn.commit()
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, ('marked', 'aasmr', self.chat_id[self.mes_count]))
                conn.commit()
        self.mes_count+=1
        self.startWorker()
    
    @Slot(str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str)
    def addCase(self, case_type, sex, age, cause, army_relations, vus, army_type,
                  army_sec_type, army_other, country, kpp, yService, voenk_region,
                  voenk_city, voenk_district, kategory, katZ, date):
        
        if case_type == '':
            self.sg.mesStatus.emit('Тип случая не может быть пустым')
            return
        
        self.case_type.append(case_type)
        self.sex.append(sex)
        self.age.append(age)
        self.cause.append(cause)
        self.army_relations.append(army_relations)
        self.vus.append(vus)
        self.army_type.append(army_type)
        self.army_sec_type.append(army_sec_type)
        self.army_other.append(army_other)
        self.country.append(country)
        self.kpp.append(kpp)
        self.yService.append(yService)
        self.voenk_region.append(voenk_region)
        self.voenk_city.append(voenk_city)
        self.voenk_district.append(voenk_district)
        self.kategory.append(kategory)
        self.katZ.append(katZ)
        self.date.append(date[:10])
        self.id.append(self.chat_mID[self.mes_count])
        
        if sex == '':
            sex = None
        if age == '':
            age = None
        if cause == '':
            cause = None
        if army_relations == '':
            army_relations = None
        if vus == '':
            vus = None
        if army_type == '':
            army_type = None
        if army_sec_type == '':
            army_sec_type = None
        if army_other == '':
            army_other = None
        if country == '':
            country = None
        if kpp == '':
            kpp = None
        if yService == '':
            yService = None
        if voenk_region == '':
            voenk_region = None
        if voenk_city == '':
            voenk_city = None
        if voenk_district == '':
            voenk_district = None
        if kategory == '':
            kategory = None
        if katZ == '':
            katZ = None
        if date == '':
            date = None
        else:
            try:
                dt_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') 
            except:
                dt_date = datetime.strptime(date, '%Y-%m-%d')      
        
        exist_query = """SELECT id FROM pograncontrol.`case` where msg_id = %s AND age = %s AND cause = %s"""
        with conn.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (self.chat_mID[self.mes_count], age, cause))
            result = cursor.fetchall()
        if len(result) > 1:
            self.sg.mesStatus.emit('Введите данные вручную')
        elif len(result) > 0:
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE pograncontrol.`case` SET msg_id = %s, case_mes_id = %s, case_type = %s, age = %s, sex = %s, cause = %s, army_relations = %s, vus = %s, army_type = %s, army_sec_type = %s, army_other = %s, country = %s, kpp = %s, yService = %s, voenk_region = %s, voenk_city = %s, voenk_district = %s, kategory_h = %s, kategory_z = %s, date = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, (self.chat_mID[self.mes_count],
                                                  self.chat_id[self.mes_count],
                                                  case_type, age, sex, cause,
                                                  army_relations, vus, army_type,
                                                  army_sec_type, army_other,
                                                  country, kpp, yService,
                                                  voenk_region, voenk_city,
                                                  voenk_district, kategory, katZ,
                                                  dt_date, result[0]))
                conn.commit()
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, ('marked', 'aasmr', self.chat_id[self.mes_count]))
                conn.commit()
        else:
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """INSERT INTO pograncontrol.`case` (msg_id, case_mes_id, case_type, age, sex, cause, army_relations, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_region, voenk_city, voenk_district, kategory_h, kategory_z, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(insert_mes_query, (self.chat_mID[self.mes_count],
                                                  self.chat_id[self.mes_count],
                                                  case_type, age, sex, cause,
                                                  army_relations, vus, army_type,
                                                  army_sec_type, army_other,
                                                  country, kpp, yService,
                                                  voenk_region, voenk_city,
                                                  voenk_district, kategory, katZ,
                                                  dt_date))
                conn.commit()
            with conn.cursor(buffered = True) as cursor:
                insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
                cursor.execute(insert_mes_query, ('marked', 'aasmr', self.chat_id[self.mes_count]))
                conn.commit()
        
        #self.mes_count+=1
        #self.startWorker()        
    def writeVbros(self): 
        with conn.cursor(buffered = True) as cursor:
            insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
            cursor.execute(insert_mes_query, ('fake', 'aasmr', self.chat_id[self.mes_count]))
            conn.commit()
        
        self.mes_count+=1
        self.startWorker() 
    
    def contWrite(self):
        with conn.cursor(buffered = True) as cursor:
            insert_mes_query = """UPDATE case_text SET tag = %s, author = %s WHERE id = %s;"""
            cursor.execute(insert_mes_query, ('pass', 'aasmr', self.chat_id[self.mes_count]))
            conn.commit()
        
        self.mes_count+=1
        self.startWorker() 
    
    def deleteRow(self):
        with conn.cursor(buffered = True) as cursor:
            insert_mes_query = """DELETE FROM case_text WHERE (id = %s);"""
            cursor.execute(insert_mes_query, (self.chat_id[self.mes_count],))
            conn.commit()
        self.mes_count+=1
        self.startWorker() 
    def showFullMes(self):
        self.window = fullMesUi(self)
        self.window.show()
        mesTextforUI =  self.dct_fullmes[self.chat_mID[self.mes_count]]
        self.sg.mesTxtFullSignal.emit(mesTextforUI)
        
    def exit(self): 
        conn.close()      
        self.uiWorker.close()

def db_connect():
    return mysql.connector.connect(host="localhost",
                                     user=input("Имя пользователя: "),
                                     password=getpass("Пароль: "),
                                     database="pograncontrol"
                                     )
def db_read_caseTable(db_con):
    exist_query = """SELECT * FROM pograncontrol.`case`;"""
    with db_con.cursor(buffered = True) as cursor:
        cursor.execute(exist_query)
        result = cursor.fetchall()
        
        msg_id = []
        case_msg_id = []
        case_type = []
        age = []
        sex = []
        cause = []
        army_relations = []
        vus = []
        army_type = []
        army_sec_type = []
        army_other = []
        country = []
        kpp = []
        yService = []
        voenk_region = []
        voenk_city = []
        voenk_district = []
        kat_h = []
        kat_z = []
        date = []
        
        for i in result:
            i = list(i)
            for j in range(1, len(i)):
                if i[j] == None:
                    i[j] = ''
            msg_id.append(i[1])      
            case_msg_id.append([2])  
            case_type.append(i[3])
            age.append(i[4])
            sex.append(i[5])
            cause.append(i[6])
            army_relations.append(i[7])
            vus.append(i[8])
            army_type.append(i[9])
            army_sec_type.append(i[10])
            army_other.append(i[11])
            country.append(i[12])
            kpp.append(i[13])
            yService.append(i[14])
            voenk_region.append(i[15])
            voenk_city.append(i[16])
            voenk_district.append(i[17])
            kat_h.append(i[18])
            kat_z.append(i[19])
            date.append(i[20])
        
    return case_type, sex, age, cause, army_relations, vus, army_type, army_sec_type, army_other, country, kpp, yService, voenk_region, voenk_city, voenk_district, kat_h, kat_z, date, msg_id, case_msg_id
def read_db_case_text(db_con):
    exist_query = """SELECT * FROM case_text"""
    with db_con.cursor(buffered = True) as cursor:
        cursor.execute(exist_query)
        result = cursor.fetchall()
        
        id = []
        msg_id = []
        date = []
        text = []
        tag = []
        author = []
        
        for i in result:
            id.append(i[0])
            msg_id.append(i[1])
            date.append(i[2])
            text.append(i[3])
            tag.append(i[4])
            author.append(i[5])
    return id, msg_id, date, text, tag, author                     

def read_db_messages_table(db_con):
    exist_query = """SELECT * FROM messages_table;"""
    with db_con.cursor(buffered = True) as cursor:
        cursor.execute(exist_query)
        res = cursor.fetchall()

    msg_txt_dict= {}
    dtime_dict = {}
    for i in res:
        msg_txt_dict[i[0]] = i[1]
        dtime_dict[i[0]] = i[2]

    return msg_txt_dict, dtime_dict

def check_db_case_text(db_con, id_text):
        exist_query = """SELECT tag FROM case_text WHERE id = %s;"""
        with db_con.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (id_text,))
            result = cursor.fetchall()
            if result == None:
                return False
            elif len(result) == 0:
                return False
            elif result[0][0] == 'marked':
                return True
            elif result[0][0] == 'pass':
                return True
            else:
                return False
def check_db_case(db_con, id_text):
        exist_query = """SELECT id FROM `case` WHERE msg_id = %s;"""
        with db_con.cursor(buffered = True) as cursor:
            cursor.execute(exist_query, (id_text,))
            result = cursor.fetchall()
            if result == None:
                return False
            elif len(result) == 0:
                return False
            else:
                return result[0][0]
if __name__ == '__main__':
    app = QApplication([])
    conn = db_connect()
    res=db_read_caseTable(conn)
    pogranworker=PogranControl(res[0], res[1], res[2], res[3], res[4], res[5],
                               res[6], res[7], res[8], res[9], res[10], res[11],
                               res[12], res[13], res[14], res[15], res[16], res[17],
                               res[18], res[19])
    res=read_db_case_text(conn)
    dct = read_db_messages_table(conn)
    pogranworker.initChatLists(res[3], res[0], res[4], res[1], dct[0], res[2])
    pogranworker.initUI()
    pogranworker.uiWorker.show()
    #pogranworker.startWorker()
    sys.exit(app.exec_())