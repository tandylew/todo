from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display_task/', views.display_task, name='display_task'),
    path('graph/', views.graph, name='graph'),
    path('login/', views.login_info, name='login_info'),
    path('park.jpg', views.park, name='park'),
]
