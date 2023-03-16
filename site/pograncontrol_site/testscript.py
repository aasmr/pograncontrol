import csv
import pandas as pd
import numpy as np
with open('case_list.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    headers_data = next(reader)
    f.close()
    case_data_prev=pd.read_csv('case_list.csv', sep=',', skiprows=1, names=headers_data)
#print(np.unique(case_data_prev['date_wo_time'], return_counts=True))
pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']

kpp_ls=pd['kpp'].fillna('').tolist()
    
for i in range(len(kpp_ls)):
    if kpp_ls[i] != 'Внуково' and kpp_ls[i] != 'Домодедово' and kpp_ls[i] != 'Шереметьево' and kpp_ls[i] != 'Пулково' and kpp_ls[i] != 'Верхний Ларс':
        kpp_ls[i] = 'Другое'
            
kpp, kpp_cnt = np.unique(kpp_ls, return_counts=True)
print(kpp, kpp_cnt)
'''
pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']
vus_lst=pd['vus'].fillna('').tolist()
for i in range(len(vus_lst)):
    if 'военная кафедра, ' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace('военная кафедра, ', '')      
    if ', военная кафедра' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', военная кафедра', '')
    if ', офицер запаса' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', офицер запаса', '')
    if 'офицер запаса, ' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace('офицер запаса, ', '')     
    if ', офицер' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', офицер', '')    
    if ', младший сержант' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', младший сержант', '')    
    if ', мл. сержант' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', мл. сержант', '')    
    if ', сержант запаса' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', сержант запаса', '')    
    if ', сержант' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', сержант', '')
    if ', контрактник' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', контрактник', '')
    if ', не служил' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace(', не служил', '')
    if 'не служил, ' in vus_lst[i]:
        vus_lst[i]=vus_lst[i].replace('не служил, ', '')
        
        
    if vus_lst[i] == 'служил' or vus_lst[i] == 'не служил' or vus_lst[i] == 'военная кафедра':
        vus_lst[i]= ''
print(vus_lst)
print(np.unique(vus_lst, return_counts=True))
'''
'''
vus, vus_cnt = np.unique(vus_pd, return_counts=True)
vus = vus[1:]
vus_cnt = vus_cnt[1:]
vus = vus.tolist()
vus_cnt = vus_cnt.tolist()

print(np.unique(vus_pd, return_counts=True))
'''

'''
for i in range(len(service)):
    if 'военная кафедра' in service[i]:
        service[i] = 'военная кафедра'
    if 'не служил' in service[i]:
        service[i] = 'не служил'
    if service[i] == '':
        service[i] = 'не указано' 
    if service[i] != 'служил' and service[i] != 'не служил' and service[i] != 'не указано' and service[i] != 'военная кафедра':
        #print(service[i])
        service[i] = 'служил' 
#    print(np.unique(service, return_counts=True))
#    if service[i] != 'служил' and service[i] != 'не служил' 
'''
