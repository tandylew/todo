from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display_task/', views.display_task, name='display_task'),
]
