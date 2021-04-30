from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def homePageView(request):
    users = User.objects.all()
    logged_user = request.user
    messages = Message.objects.filter(receiver=logged_user)
    context = {
        'users': users,
        'messages': messages
        }
    return render(request, 'home.html', context)


@login_required
@csrf_exempt
def sendMessageView(request):
    sender = User.objects.get(username=request.user)
    receiver = request.POST.get('receiver')
    content = request.POST.get('message')

    Message.objects.create(sender=sender, receiver=receiver, message_content=content)
    
    return redirect('/')

@login_required
def deleteMessageView(request):
    id = request.POST.get('id')
    message_to_delete = Message.objects.get(pk=id)
    message_to_delete.delete()
    return redirect('/')

@login_required
def searchMessageView(request):
    search = request.GET['query']
    
    query = "SELECT * FROM pages_message WHERE receiver = '%s' AND (sender LIKE '%%%s%%' OR message_content LIKE '%%%s%%')" % (request.user,search,search)
    messages = Message.objects.raw(query)

    context = {
        'messages': messages,
    }
    
    return render(request, 'search.html', context)