from django.urls import path
from . import views
from EDA.dash_apps.finished_apps import genderCD4, jobCD4

urlpatterns = [
    path('', views.show, name='EDA')
]