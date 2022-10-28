'''
Created on 28 окт. 2022 г.

@author: aasmr
'''
import json
import logging
import os.path
import pandas as pd
import csv
        
chatContent_file = open('./result.json', 'r', encoding="utf8")
chatContent = chatContent_file.read()
chatContent_JSON=json.loads(chatContent)

chat_messages = chatContent_JSON['messages']

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
    date = case_data_prev['date'].tolist()
    id = case_data_prev['id'].tolist()
else: 
    age = []
    cause = []
    vus = []
    country = []
    kpp = []
    date = []
    id = []
                        
try:
    for mes in chat_messages:
        if mes['id'] not in id:
            if mes['id'] > id[-1]:
                for mes_content in mes['text']:
                    if  isinstance (mes_content, dict):
                        if mes_content['type'] == 'text_link' or mes_content['type'] == 'hashtag':
                            if mes_content['text'] == '#развернули':
                                print(mes['text'])
                                print(mes_content)
                                print(mes['text'][mes['text'].index(mes_content)+1])
                                age_in = input('Возраст: ')
                                if age_in == 'cont':
                                    continue
                                else:
                                    age.append(age_in)
                                cause.append(input('Причина: '))
                                vus.append(input('ВУС: '))
                                country.append(input('Страна въезда: '))
                                kpp.append(input('КПП выезда: '))
                                print(mes['date'])
                                date_in=input('Дата: ')
                                if date_in =='':
                                    date.append(mes['date'])
                                else:
                                    date.append(date_in)
                                id.append(mes['id'])
    
                        #print(i)
                    elif isinstance (mes_content, str):
                        if '❌' in mes_content:
                            print(mes['text'])
                            print(mes_content)
                            age_in = input('Возраст: ')
                            if age_in == 'cont':
                                continue
                            else:
                                age.append(age_in)
                            cause.append(input('Причина: '))
                            vus.append(input('ВУС: '))
                            country.append(input('Страна въезда: '))
                            kpp.append(input('КПП выезда: '))
                            print(mes['date'])
                            date_in=input('Дата: ')
                            if date_in =='':
                                date.append(mes['date'])
                            else:
                                date.append(date_in)
                            id.append(mes['id'])                
                    else:
                        if '❌' in mes_content:
                            print(mes['text'])
                            print(mes_content)
                            age_in = input('Возраст: ')
                            if age_in == 'cont':
                                continue
                            else:
                                age.append(age_in)
                            cause.append(input('Причина: '))
                            vus.append(input('ВУС: '))
                            country.append(input('Страна въезда: '))
                            kpp.append(input('КПП выезда: '))
                            print(mes['date'])
                            date_in=input('Дата: ')
                            if date_in =='':
                                date.append(mes['date'])
                            else:
                                date.append(date_in)
                            id.append(mes['id'])                     
except EOFError:
    print(mes['id'])
    df={'id':id, 'age':age, 'cause':cause, 'vus':vus, 'country':country, 'kpp':kpp, 'date':date}
    negative_case_data=pd.DataFrame(df)
    with open('case_list.csv', 'w', encoding="utf-8") as f:
        #csv=s.sort_values('cnt')
        f.write(negative_case_data.to_csv(index=True))
        f.close()             
except Exception as e:
    logging.error(e, exc_info=True)
    print(mes['id'])
    df={'id':id, 'age':age, 'cause':cause, 'vus':vus, 'country':country, 'kpp':kpp, 'date':date}
    negative_case_data=pd.DataFrame(df)
    with open('case_list.csv', 'w', encoding="utf-8") as f:
        #csv=s.sort_values('cnt')
        f.write(negative_case_data.to_csv(index=True))
        f.close() 
        
df={'id':id, 'age':age, 'cause':cause, 'vus':vus, 'country':country, 'kpp':kpp, 'date':date}
negative_case_data=pd.DataFrame(df)
with open('case_list.csv', 'w', encoding="utf-8") as f:
    #csv=s.sort_values('cnt')
    f.write(negative_case_data.to_csv(index=True))
    f.close()
     
if __name__ == '__main__':
    pass