from django.urls import path
from pogran_visualisation import views

urlpatterns = [
    path('', views.home, name='home'),
    path('otkaz/', views.otkaz_chart, name='otkaz'),
    path('sluzhba/', views.sluzhba_chart, name='sluzhba'),
    path('sex/', views.sex_chart, name='sex'),
    path('age/', views.age_chart, name='age'),
    path('kpp/', views.kpp_chart, name='kpp')
]
