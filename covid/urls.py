from django.contrib import admin
from django.urls import path
from covid import views                                     # !!!

urlpatterns = [
    path('covid/',
         views.covid, name='covid'),
    path('covid2/',
         views.covid2, name='covid2'),
    # !!!
]