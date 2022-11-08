from django.urls import path
from pogran_visualisation import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.population_chart, name='dashboard')
]
