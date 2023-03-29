"""siemanko"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #strona główna.
    path('',views.index, name='index'),
    #path('stópka',views.index, name='stópka')
    path('topics/', views.topics, name='topics'),
]