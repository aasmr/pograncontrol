import csv
import pandas as pd
import numpy as np
with open('case_list.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    headers_data = next(reader)
    f.close()
    case_data_prev=pd.read_csv('case_list.csv', sep=',', skiprows=1, names=headers_data)
#print(np.unique(case_data_prev['date_wo_time'], return_counts=True))

pd=case_data_prev['cause'].fillna('none')
print(np.unique(pd, return_counts=True))
#print(pd)