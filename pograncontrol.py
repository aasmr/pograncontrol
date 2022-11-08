'''
Created on 28 окт. 2022 г.

@author: aasmr
'''
import json
import logging
import os.path
import pandas as pd
import csv
import sys

from pograncontrol.pogran_ui import *

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
    mesDateSignal = Signal(str, str)
    def __init__(self):
        super().__init__()

class PogranControl():
    def __init__(self, age = [], cause = [], vus = [], country = [], kpp = [], yService = [], voenk = [], kategory = [], katZ = [], date = [], id_ls = []):
        self.age = age
        self.cause = cause
        self.vus = vus
        self.country = country
        self.kpp = kpp
        self.yService = yService
        self.voenk = voenk
        self.kategory = kategory
        self.katZ = katZ
        self.date = date
        self.id = id_ls
        
        self.mes_count=0
        
    def initChatLists(self, mes, cont_id=[], cont_tag=[]):
        self.chat_mes = mes
        self.cont_id = cont_id
        self.cont_tag = cont_tag
        
    
    def initUI(self):
        
        self.sg = Signals()
        self.uiWorker = ui(self)
        self.uiWorker.sg.endInitSignal.connect(self.startWorker)
        self.uiWorker.sg.writeSignal.connect(self.writecase)
        self.uiWorker.sg.addSignal.connect(self.addCase)
        self.uiWorker.exitBut.clicked.connect(self.exit) 
        self.uiWorker.contBut.clicked.connect(self.contWrite)
        self.uiWorker.vbrosBut.clicked.connect(self.writeVbros)
        
        self.uiWorker.sg.endInitSignal.emit()
        #self.uiWorker.contBut.clicked.connect(self.startWorker)
        
    def startWorker(self):
        try:
            flag=1
            while flag:
                if self.chat_mes[self.mes_count]['id'] not in self.cont_id:
                    mesTextforUI = ''
                    for mes_content in self.chat_mes[self.mes_count]['text']:
                        if  isinstance (mes_content, dict):
                            # if '#развернули' in mes_content['text'] or '❌' in mes_content['text']:
                            #     mesTextforUI = mesTextforUI + '**' + mes_content['text'] + '**'
                            # else:
                            mesTextforUI += mes_content['text']
                        else:
                            mesTextforUI += mes_content
                    if '#развернули' in mesTextforUI or '❌' in mesTextforUI:
                        self.sg.mesTxtSignal.emit(mesTextforUI)
                        msgCnt=str(self.mes_count) + '/' + str(len(self.chat_mes))
                        self.sg.mesDateSignal.emit(self.chat_mes[self.mes_count]['date'], msgCnt)
                        #print(mesTextforUI)
                        flag=0;
                    else:
                        self.cont_id.append(self.chat_mes[self.mes_count]['id'])
                        self.cont_tag.append('cont')
                        self.mes_count+=1
                else:
                    self.mes_count+=1
                                    
        except EOFError:
            #print(mes['id'])
            df={'id':self.id, 'age':self.age, 'cause':self.cause, 'vus':self.vus,
             'country':self.country, 'kpp':self.kpp, 'yService':self.yService,
              'voenk':self.voenk, 'kategory':self.kategory, 'katZ':self.katZ, 'date':self.date}
            negative_case_data=pd.DataFrame(df)
            with open('case_list.csv', 'w', encoding="utf-8") as f:
                #csv=s.sort_values('cnt')
                f.write(negative_case_data.to_csv(index=True))
                f.close()
            
            df={'id': self.cont_id, 'tag':self.cont_tag}
            cont_data=pd.DataFrame(df)
            with open('continue_list.csv', 'w', encoding="utf-8") as f:
                #csv=s.sort_values('cnt')
                f.write(cont_data.to_csv(index=True))
                f.close()
                             
        except Exception as e:
            print(e)
            df={'id':self.id, 'age':self.age, 'cause':self.cause, 'vus':self.vus,
             'country':self.country, 'kpp':self.kpp, 'yService':self.yService,
              'voenk':self.voenk, 'kategory':self.kategory, 'katZ':self.katZ, 'date':self.date}
            negative_case_data=pd.DataFrame(df)
            with open('case_list.csv', 'w', encoding="utf-8") as f:
                #csv=s.sort_values('cnt')
                f.write(negative_case_data.to_csv(index=True))
                f.close()
            
            df={'id': self.cont_id, 'tag':self.cont_tag}
            cont_data=pd.DataFrame(df)
            with open('continue_list.csv', 'w', encoding="utf-8") as f:
                #csv=s.sort_values('cnt')
                f.write(cont_data.to_csv(index=True))
                f.close()
    
    @Slot(str, str, str, str, str, str, str, str, str, str)
    def writecase(self, age, cause, vus, country, kpp, yService, voenk, kategory, katZ, date):
        self.age.append(age)
        self.cause.append(cause)
        self.vus.append(vus)
        self.country.append(country)
        self.kpp.append(kpp)
        self.yService.append(yService)
        self.voenk.append(voenk)
        self.kategory.append(kategory)
        self.katZ.append(katZ)
        self.date.append(date)
        self.id.append(self.chat_mes[self.mes_count]['id'])
        
        self.cont_id.append(self.chat_mes[self.mes_count]['id'])
        self.cont_tag.append('negative')
        
        self.mes_count+=1
        self.startWorker()
    
    @Slot(str, str, str, str, str, str, str, str, str, str)
    def addCase(self, age, cause, vus, country, kpp, yService, voenk, kategory, katZ, date):
        self.age.append(age)
        self.cause.append(cause)
        self.vus.append(vus)
        self.country.append(country)
        self.kpp.append(kpp)
        self.yService.append(yService)
        self.voenk.append(voenk)
        self.kategory.append(kategory)
        self.katZ.append(katZ)
        self.date.append(date)
        self.id.append(self.chat_mes[self.mes_count]['id'])
        
        self.cont_id.append(self.chat_mes[self.mes_count]['id'])
        self.cont_tag.append('negative')
        
        #self.mes_count+=1
        #self.startWorker()        
    def writeVbros(self):
        
        self.cont_id.append(self.chat_mes[self.mes_count]['id'])
        self.cont_tag.append('vbros')
        
        self.mes_count+=1
        self.startWorker()
    
    def contWrite(self):
        self.cont_id.append(self.chat_mes[self.mes_count]['id'])
        self.cont_tag.append('cont')
        
        self.mes_count+=1
        self.startWorker() 
          
    def exit(self): 
        df={'id':self.id, 'age':self.age, 'cause':self.cause, 'vus':self.vus,
             'country':self.country, 'kpp':self.kpp, 'yService':self.yService,
              'voenk':self.voenk, 'kategory':self.kategory, 'katZ':self.katZ, 'date':self.date}
        negative_case_data=pd.DataFrame(df)
        with open('case_list.csv', 'w', encoding="utf-8") as f:
            #csv=s.sort_values('cnt')
            f.write(negative_case_data.to_csv(index=True))
            f.close()
        
        df={'id': self.cont_id, 'tag':self.cont_tag}
        cont_data=pd.DataFrame(df)
        with open('continue_list.csv', 'w', encoding="utf-8") as f:
            #csv=s.sort_values('cnt')
            f.write(cont_data.to_csv(index=True))
            f.close()
        
        self.uiWorker.close()

# df={'id':id, 'age':age, 'cause':cause, 'vus':vus, 'country':country, 'kpp':kpp, 'date':date}
# negative_case_data=pd.DataFrame(df)
# with open('case_list.csv', 'w', encoding="utf-8") as f:
#     #csv=s.sort_values('cnt')
#     f.write(negative_case_data.to_csv(index=True))
#     f.close()
        
def openFiles():
    
    if os.path.isfile('case_list.csv'):
        with open('case_list.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=',')
            headers_data = next(reader)
            f.close()
            case_data_prev=pd.read_csv('case_list.csv', sep=',', skiprows=1, names=headers_data)
            age = case_data_prev['age'].tolist()
            cause = case_data_prev['cause'].tolist()
            vus = case_data_prev['vus'].tolist()
            country = case_data_prev['country'].tolist()
            kpp = case_data_prev['kpp'].tolist()
            yService=case_data_prev['yService'].tolist()
            voenk=case_data_prev['voenk'].tolist()
            kategory=case_data_prev['kategory'].tolist()
            katZ=case_data_prev['katZ'].tolist()
            date = case_data_prev['date'].tolist()
            id = case_data_prev['id'].tolist()
            pogranworker=PogranControl(age, cause, vus, country, kpp, yService, voenk, kategory, katZ, date, id)
    else: 
        pogranworker=PogranControl()
    
    if os.path.isfile('continue_list.csv'):
        with open('continue_list.csv', 'r', encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=',')
            headers_data = next(reader)
            f.close()
            cont_data_prev=pd.read_csv('continue_list.csv', sep=',', skiprows=1, names=headers_data)
            cont_id = cont_data_prev['id'].tolist()
            cont_tag = cont_data_prev['tag'].tolist()
    else: 
        cont_id = []
        cont_tag = []
    
    chatContent_file = open('./result.json', 'r', encoding="utf8")
    chatContent = chatContent_file.read()
    chatContent_JSON=json.loads(chatContent)
    
    chat_messages = chatContent_JSON['messages']
    
    pogranworker.initChatLists(chat_messages, cont_id, cont_tag)        
    return pogranworker
                      

     
if __name__ == '__main__':
    app = QApplication([])
    pogranworker=openFiles()
    pogranworker.initUI()
    pogranworker.uiWorker.show()
    #pogranworker.startWorker()
    sys.exit(app.exec_())