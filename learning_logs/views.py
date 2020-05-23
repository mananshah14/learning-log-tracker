from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404




from . models import Topic
from . models import Entry
from .forms import TopicForm 
from .forms import EntryForm

# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
     #show all topics
     topics = Topic.objects.filter(owner=request.user).order_by('date_added')
        
     context = {'topics':topics}
     return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request , topic_id):
    # show a single topic and all its enteries
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic , 'entries' : entries }
    return render(request , 'learning_logs/topic.html' , context)    
     
@login_required
def new_topic(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm() 
    else:
        form  = TopicForm(request.POST) # if data entered
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form' : form}
    return render(request , 'learning_logs/new_topic.html' , context) 

@login_required
def new_entry(request , topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm() 
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}     
    return render(request, 'learning_logs/edit_entry.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})
 

    







    
    
    
    
    
    
    
    
    
    
         
 