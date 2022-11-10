from django.urls import path
from pogran_visualisation import views

urlpatterns = [
    path('', views.home, name='home'),
    path('otkaz/', views.otkaz_chart, name='otkaz'),
    path('sluzhba/', views.sluzhba_chart, name='sluzhba')
]
