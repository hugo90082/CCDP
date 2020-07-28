from django.urls import path
from . import views
from EDA.dash_apps.finished_apps import genderCD4, jobCD4, industryCD4, eduCD4, homeOwnershipCD4

urlpatterns = [
    path('', views.interactivePlot, name='interactive_Plot'),
    path('basic_statistic/', views.basicStatistic, name='basic_statistic'),
    path('our_model/', views.ourModel, name='our_model'),
]
