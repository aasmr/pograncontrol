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
    #csv_to_db()
    #q=Pograncontrol.objects.unique('date'))
    #print(Pograncontrol.objects.unique('date'))
    
    labels, data = np.unique(case_data_prev['date_wo_time'], return_counts=True)
    for i in labels:
        labels_.append(str(i))
    for i in data:
        data_.append(str(i))
    return JsonResponse(data={
        'labels': labels_,
        'data': data_,
        })

        
