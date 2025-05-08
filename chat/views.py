from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details, created = Room.objects.get_or_create(name = room)
    return render(request, 'room.html', {
        'username': username,
        'room' : room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect(f'/{room}/?username={username}')
    else:
        new_room = Room.objects.create(name= room)
        new_room.save()
        return redirect(f'/{room}/?username={username}')
    

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value = message, 
        user = username, 
        room = Room.objects.get(id=room_id)
        )
    new_message.save()
    return HttpResponse('Message envoyé avec succès')


def getMessages(request, room):
    
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details).order_by('date')
    return JsonResponse(
        {
        "messages": [
            {
                "user": msg.user,
                "value": msg.value,
                "date": msg.date.strftime("%Y-%m-%d %H:%M:%S")
            }
            for msg in messages
        ]
    }
    )