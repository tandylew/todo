from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_list/', views.create_list, name='create_list'),
    path('create_list_item/', views.create_list_item, name='create_list_item'),
    path('delete_list/', views.delete_list, name='delete_list'),
]