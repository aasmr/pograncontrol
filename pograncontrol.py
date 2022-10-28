'''
Created on 28 окт. 2022 г.

@author: aasmr
'''
import json
import logging

class NegativeCase:
    def __init__(self, age, cause, vus, country, kpp, date, id):
        self.age = age
        self.cause = cause
        self.vus = vus
        self.country = country
        self.kpp = kpp
        self.date = date
        self.id = id
        
chatContent_file = open('./result.json', 'r', encoding="utf8")
chatContent = chatContent_file.read()
chatContent_JSON=json.loads(chatContent)

chat_messages = chatContent_JSON['messages']

case_list=[]
indx_off = 0
indx_on = 0
try:
    for mes in chat_messages:
        for mes_content in mes['text']:
            if  isinstance (mes_content, dict):
                if mes_content['type'] == 'text_link' or mes_content['type'] == 'hashtag':
                    if mes_content['text'] == '#развернули':
                        print(mes['text'])
                        print(mes_content)
                        age = input('Возраст: ')
                        cause = input('Причина: ')
                        vus = input('ВУС: ')
                        country = input('Страна въезда: ')
                        kpp = input('КПП выезда: ')
                        date=mes['date']
                        id = mes['id']
                        case_list.append(NegativeCase(age, cause, vus, country, kpp, date, id))
                    else:
                        mes['text'].remove(mes_content)
                else:
                    mes['text'].remove(mes_content)
                #print(i)
            elif isinstance (mes_content, str):
                if '❌' in mes_content:
                    print(mes['text'])
                    print(mes_content)
                    age = input('Возраст: ')
                    cause = input('Причина: ')
                    vus = input('ВУС: ')
                    country = input('Страна въезда: ')
                    kpp = input('КПП выезда: ')
                    date=mes['date']
                    id = mes['id']
                    case_list.append(NegativeCase(age, cause, vus, country, kpp, date, id))
            else:
                if '❌' in mes_content:
                    print(mes['text'])
                    print(mes_content)
                    age = input('Возраст: ')
                    cause = input('Причина: ')
                    vus = input('ВУС: ')
                    country = input('Страна въезда: ')
                    kpp = input('КПП выезда: ')
                    date=mes['date']
                    id = mes['id']
                    case_list.append(NegativeCase(age, cause, vus, country, kpp, date, id))
                
except Exception as e:
    logging.error(e, exc_info=True)
    with open('case_list', 'wb', encoding="utf-8") as f:
        f.write(case_list)
        f.close() 
#     #print(adr_split)
#     df={'id':uik_n, 'code':code_n, 'region':reg_n, 'district':dist_n}
#     uik_district_data=pd.DataFrame(df)
#     with open('uik_data.csv', 'w', encoding="utf-8") as f:
#         #csv=s.sort_values('cnt')
#         f.write(uik_district_data.to_csv(index=True))
#         f.close() 
if __name__ == '__main__':
    pass