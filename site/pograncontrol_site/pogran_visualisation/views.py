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
    
    other_data_ = []
    otkaz_voenk_data_ = []
    otkaz_country_data_ = []
    otkaz_country_exit_data_ = []
    #csv_to_db()
    #q=Pograncontrol.objects.unique('date'))
    #print(Pograncontrol.objects.unique('date'))
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']
    otkaz_voenk_label, otkaz_voenk_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    pd=case_data_prev[case_data_prev['cause'] == 'отказ во въезде']
    otkaz_country_label, otkaz_country_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    pd=case_data_prev[case_data_prev['cause'] == 'отказ в выезде иностранным государством']
    otkaz_country_exit_label, otkaz_country_exit_data = np.unique(pd['date_wo_time'], return_counts=True)
    
    labels, data = np.unique(case_data_prev['date_wo_time'], return_counts=True)
    for i in labels:
        labels_.append(str(i))
    for i in data:
        data_.append(str(i))
    for i in otkaz_voenk_data:
        otkaz_voenk_data_.append(str(i))
    for i in otkaz_country_data:
        otkaz_country_data_.append(str(i))
    for i in otkaz_country_exit_data:
        otkaz_country_exit_data_.append(str(i))

    i=0
    while i < len(labels):
        if not (labels[i] in otkaz_country_label):
            otkaz_country_data_.insert(i, str(0))
        if not (labels[i] in otkaz_country_exit_label):
            otkaz_country_exit_data_.insert(i, str(0))
        if not (labels[i] in otkaz_voenk_label):
            otkaz_voenk_data_.insert(i, str(0))
        
        other_data_.insert(i,(int(data_[i])-int(otkaz_voenk_data_[i])-
                              int(otkaz_country_exit_data_[i])-int(otkaz_country_data_[i])))
        i+=1   
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        'voenk': otkaz_voenk_data_,
        'country': otkaz_country_data_,
        'exit': otkaz_country_exit_data_,
        'other': other_data_
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

def sex_chart(request):
    labels_=[]
    data_=[]
    pd=case_data_prev

    sex=pd['yService'].fillna('').tolist()

    for i in range(len(sex)):
        if 'женщина' in sex[i]:
            sex[i] = 'женщина'
        else:
            sex[i] = 'мужчина'

    labels, data = np.unique(sex, return_counts=True)
    
    for i in labels:
        labels_.append(str(i))
    for i in data:
        data_.append(str(i))
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        })

def age_chart(request):
    labels_=[]
    data_=[]
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']

    age=pd['age'].fillna('').tolist()
    age, age_cnt = np.unique(age, return_counts=True)
    age = age[1:]
    age_cnt = age_cnt[1:]
    age = age.tolist()
    age_cnt = age_cnt.tolist()
    for i in range(len(age)):
        age[i] = int(float(age[i]))

    i=0

    l_cnt = len(age)
    while i < l_cnt-1:
        if age[i+1] - age[i] > 1:
            age.insert(i+1, age[i]+1)
            age_cnt.insert(i+1, 0)
        i=i+1
        l_cnt = len(age)
    
    for i in age:
        labels_.append(str(i))
    for i in age_cnt:
        data_.append(str(i))
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        })
    
def kpp_chart(request):
    labels_=[]
    data_=[]
    pd=case_data_prev[case_data_prev['cause'] == 'отказ от военкомата']

    kpp_ls=pd['kpp'].fillna('').tolist()
    
    for i in range(len(kpp_ls)):
        if kpp_ls[i] != 'Внуково' and kpp_ls[i] != 'Домодедово' and kpp_ls[i] != 'Шереметьево' and kpp_ls[i] != 'Пулково' and kpp_ls[i] != 'Верхний Ларс':
            kpp_ls[i] = 'Другое'
            
    kpp, kpp_cnt = np.unique(kpp_ls, return_counts=True)
    kpp = kpp.tolist()
    kpp_cnt = kpp_cnt.tolist()
    
    for i in kpp:
        labels_.append(str(i))
    for i in kpp_cnt:
        data_.append(str(i))
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        })

