import pandas as pd
from datetime import datetime
import csv
from .models import Pograncontrol

# dataset from https://www.kaggle.com/aungpyaeap/supermarket-sales
# headers changed and invoice number col removed
def csv_to_db():
    with open('pogran.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        headers_data = next(reader)
        f.close()
        case_data_prev=pd.read_csv('pogran.csv', sep=',', skiprows=1, names=headers_data)
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

        for i in range(len(age)):
            pograncontrol = Pograncontrol(
            age = age[i],
            cause = cause[i],
            vus = vus[i],
            country = country[i],
            kpp = kpp[i],
            yService = yService[i],
            voenk = voenk[i],
            kategory = kategory[i],
            katZ = katZ[i],
            date  = datetime.strptime(date[i],'%Y-%m-%dT%H:%M:%S').date()
        )
        pograncontrol.save()
