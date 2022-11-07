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

class ui_thread(QThread):

    def __init__(self, pogranWorker):
        super().__init__()
        self.pogran = pogranWorker
    
    ###################
    #Разобраться, нахера это нужно
    ###################   
    def __del__(self):
        self.wait()
    
    ###################
    #Тело потока
    ###################      
    def run(self):
        self.running = True #Флаг работы потока
        while self.running:
            try:
                for mes in self.pogran.chat_mes:
                    if mes['id'] not in self.pogran.cont_id:
                        mesTextforUI = ''
                        for mes_content in mes['text']:
                            if  isinstance (mes_content, dict):
                                mesTextforUI += mes_content['text']
                            else:
                                mesTextforUI += mes_content
                        self.pogran.sg.mesTxtSignal.emit(mesTextforUI)
                            #self.uiWorker.setMes(mesTextforUI)
                        print(mesTextforUI)
                        input()
                            #     if mes_content['type'] == 'text_link' or mes_content['type'] == 'hashtag':
                            #         if mes_content['text'] == '#развернули':
                            #             print(mes['text'])
                            #             print(mes_content)
                            #             print(mes['text'][mes['text'].index(mes_content)+1])
                            #             age_in = input('Возраст: ')
                            #             if age_in == 'cont':
                            #                 continue
                            #             else:
                            #                 age.append(age_in)
                            #             cause.append(input('Причина: '))
                            #             vus.append(input('ВУС: '))
                            #             country.append(input('Страна въезда: '))
                            #             kpp.append(input('КПП выезда: '))
                            #             print(mes['date'])
                            #             date_in=input('Дата: ')
                            #             if date_in =='':
                            #                 date.append(mes['date'])
                            #             else:
                            #                 date.append(date_in)
                            #             id.append(mes['id'])
                            #
                            #     #print(i)
                            # elif isinstance (mes_content, str):
                            #     if '❌' in mes_content:
                            #         print(mes['text'])
                            #         print(mes_content)
                            #         age_in = input('Возраст: ')
                            #         if age_in == 'cont':
                            #             continue
                            #         else:
                            #             age.append(age_in)
                            #         cause.append(input('Причина: '))
                            #         vus.append(input('ВУС: '))
                            #         country.append(input('Страна въезда: '))
                            #         kpp.append(input('КПП выезда: '))
                            #         print(mes['date'])
                            #         date_in=input('Дата: ')
                            #         if date_in =='':
                            #             date.append(mes['date'])
                            #         else:
                            #             date.append(date_in)
                            #         id.append(mes['id'])                
                            # else:
                            #     if '❌' in mes_content:
                            #         print(mes['text'])
                            #         print(mes_content)
                            #         age_in = input('Возраст: ')
                            #         if age_in == 'cont':
                            #             continue
                            #         else:
                            #             age.append(age_in)
                            #         cause.append(input('Причина: '))
                            #         vus.append(input('ВУС: '))
                            #         country.append(input('Страна въезда: '))
                            #         kpp.append(input('КПП выезда: '))
                            #         print(mes['date'])
                            #         date_in=input('Дата: ')
                            #         if date_in =='':
                            #             date.append(mes['date'])
                            #         else:
                            #             date.append(date_in)
                            #         id.append(mes['id'])                     
            except EOFError:
                #print(mes['id'])
                df={'id':self.id, 'age':self.age, 'cause':self.cause, 'vus':self.vus,
                     'country':self.country, 'kpp':self.kpp, 'yService':self.yService,
                      'voenk':self.voenk, 'date':self.date}
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
                      'voenk':self.voenk, 'date':self.date}
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
            
        
sys.excepthook = log_uncaught_exceptions 

class Signals(QObject):
    mesTxtSignal = Signal(str)
    mesDateSignal = Signal(str)
    def __init__(self):
        super().__init__()

class PogranControl():
    def __init__(self, age = [], cause = [], vus = [], country = [], kpp = [], yService = [], voenk = [], date = [], id_ls = []):
        self.age = age
        self.cause = cause
        self.vus = vus
        self.country = country
        self.kpp = kpp
        self.yService = yService
        self.voenk = voenk
        self.date = date
        self.id = id_ls
        
        self.thr = ui_thread(self);
    def initChatLists(self, mes, cont_id=[], cont_tag=[]):
        self.chat_mes = mes
        self.cont_id = cont_id
        self.cont_tag = cont_tag
        
    
    def initUI(self):
        
        self.sg = Signals()
        self.uiWorker = ui(self)
        self.uiWorker.sg.endInitSignal.connect(self.startWorker)  
        #self.uiWorker.sg.endInitSignal.emit()
        
    @Slot()
    def startWorker(self):
        self.thr.run()
        
#
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
            date = case_data_prev['date'].tolist()
            id = case_data_prev['id'].tolist()
            pogranworker=PogranControl(age, cause, vus, country, kpp, yService, voenk, date, id)
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