from django.urls import path, include
from razmetka import views

urlpatterns = [
    path('', views.razmetka_page, name='razmetka_page'),
    path('get-mes/', views.get_mes_info, name='get-mes'),
    path('get-dup/', views.get_duplicate, name='get-dup'),
    path('get-marked/', views.get_marked, name='get-marked'),
    path('auth/', views.auth, name='auth'),
    path('auth/', include('django.contrib.auth.urls')),
    path('autocmplt/', views.autocmplt, name='autocmplt'),
    path('add/', views.add, name='add'),
    path('add-more/', views.add_more, name='add-more'),
    path('pass/', views.pass_mes, name='pass'),
    path('vbros/', views.vbros, name='vbros'),
    path('del/', views.del_case, name='del')
]
#path('auth/login/', views._login, name='login'),
