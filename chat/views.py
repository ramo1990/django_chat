from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return redirect('/')
    
    print(f"Room details: {room_details}")

    return render(request, 'room.html', {
        'username':username, 'room':room, "room_details":room_details
    })

def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')

    print("room:", room)
    print("username:", username)

    if not room or not username:
        return redirect('/')
    
    Room.objects.get_or_create(name=room)

    url = f'/{room}/?username={username}'
    print('redirect debug:', url)
    return redirect(url)
    
def getMessages(request, room):
    try:
        room_obj = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room not found"}, status=404)

    messages = Message.objects.filter(room=room_obj).order_by('date')

    message_list = []
    for message in messages:
        message_list.append({
            'user': message.user,
            'value': message.value,
            'date': message.date
        })
    print(f"Messages for room {room}: {message_list}")
    return JsonResponse({"messages": message_list})

@csrf_exempt
def send(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')
        message = request.POST.get('message')

        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return JsonResponse({"error":"Room not found"}, status=404)

        new_message = Message.objects.create(
            value = message,
            user = username,
            room = room
        )
        new_message.save()
        return JsonResponse({'status':'Message envoyé avec succès'})
