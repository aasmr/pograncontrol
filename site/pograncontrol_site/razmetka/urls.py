from django.urls import path, include
from razmetka import views

urlpatterns = [
    path('', views.razmetka_page, name='razmetka_page'),
    path('auth/', views.auth, name='auth'),
    path('auth/', include('django.contrib.auth.urls')),
    path('autocmplt/', views.autocmplt, name='autocmplt'),
    path('add/', views.add, name='add'),
]
#path('auth/login/', views._login, name='login'),
