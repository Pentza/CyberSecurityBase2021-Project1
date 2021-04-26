from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required

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
def sendMessageView(request):
    sender = User.objects.get(username=request.user)
    receiver = request.POST.get('receiver')
    content = request.POST.get('message')
    
    message_obj = Message.objects.create(sender=sender, receiver=receiver, message_content=content)
    return redirect('/')

@login_required
def deleteMessageView(request):
    id = request.POST.get('id')
    message_to_delete = Message.objects.get(pk=id)
    message_to_delete.delete()
    return redirect('/')