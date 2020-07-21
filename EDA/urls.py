from django.urls import path
from . import views
from EDA.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.show, name='EDA')
]