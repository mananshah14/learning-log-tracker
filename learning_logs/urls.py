# -*- coding: utf-8 -*-


from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    #home page 
    path('' , views.index, name ='index'),    
    
    path('new_topic/', views.new_topic, name='new_topic'),
    
    
     # Show all topics.
    path('topics' , views.topics, name='topics'),
    #detail page for a specific topic 
    path(r'<int:topic_id>', views.topic, name='topic'),
    #page for adding a new topic
    
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    
    
]

