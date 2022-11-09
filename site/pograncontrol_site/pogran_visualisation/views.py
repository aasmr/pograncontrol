from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from .methods import csv_to_db
from .models import Pograncontrol
import pandas as pd
import csv
import numpy as np

with open('case_list.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    headers_data = next(reader)
    f.close()
    case_data_prev=pd.read_csv('case_list.csv', sep=',', skiprows=1, names=headers_data)

def home(request):
    return render(request, 'dashboard.html')
    
def population_chart(request):
    # get the data from the default method       
    #context = super().get_context_data(**kwargs)
    labels_=[]
    data_=[]
    
    otkaz_voenk_label_ = []
    otkaz_voenk_data_ = []
    #csv_to_db()
    #q=Pograncontrol.objects.unique('date'))
    #print(Pograncontrol.objects.unique('date'))
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']
    
    labels, data = np.unique(case_data_prev['date_wo_time'], return_counts=True)
    otkaz_voenk_label, otkaz_voenk_data = np.unique(pd['date_wo_time'], return_counts=True)
    for i in labels:
        labels_.append(str(i))
    for i in data:
        data_.append(str(i))
    for i in otkaz_voenk_data:
        otkaz_voenk_data_.append(str(i))
    i = 0    
    while otkaz_voenk_label[0] > labels[i]:
        otkaz_voenk_data_.insert(0, str(0))
        i+=1
    
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        'voenk': otkaz_voenk_data_
        })

        
