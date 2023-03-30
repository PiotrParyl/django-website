from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """siemanko"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """siemanko"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def stopka(request):
    """siemanko"""
    
    return render(request, 'learning_logs/stopka.html')

def topic(request, topic_id):
    """siemanko"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)