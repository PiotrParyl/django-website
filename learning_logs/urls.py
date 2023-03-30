"""siemanko"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #strona główna.
    path('',views.index, name='index'),
    path('stopka/',views.stopka, name='stopka'),
    path('topics/', views.topics, name='topics'),
]