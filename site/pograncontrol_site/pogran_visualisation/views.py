from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from .methods import csv_to_db
from .models import Pograncontrol
import pandas as pd
import csv
import numpy as np
from django.template.context_processors import request

with open('case_list.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    headers_data = next(reader)
    f.close()
    case_data_prev=pd.read_csv('case_list.csv', sep=',', skiprows=1, names=headers_data)

def home(request):
    return render(request, 'dashboard.html')
    
def otkaz_chart(request):
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
    otkaz_voenk_label, otkaz_voenk_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    pd=case_data_prev[case_data_prev['cause'] == 'отказ во въезде']
    otkaz_country_label, otkaz_country_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от въезде']
    otkaz_country_exit_label, otkaz_country_exit_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    labels, data = np.unique(case_data_prev['date_wo_time'], return_counts=True)
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

def sluzhba_chart(request):
    labels_=[]
    data_=[]
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']

    service=pd['vus'].fillna('').tolist()

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

    labels, data = np.unique(service, return_counts=True)
    
    for i in labels:
        labels_.append(str(i))
    for i in data:
        data_.append(str(i))
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        })
