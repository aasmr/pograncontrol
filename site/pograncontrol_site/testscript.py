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

service=pd['vus'].fillna('').tolist()
print(np.unique(service, return_counts=True))
#print(service)

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