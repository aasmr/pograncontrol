from django.urls import path
from razmetka import views

urlpatterns = [
    path('', views.razmetka_page, name='razmetka_page'),
    path('login/', views.login, name='login'),
]
