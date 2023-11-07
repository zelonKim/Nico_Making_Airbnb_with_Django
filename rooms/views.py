from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def see_all_rooms(request):  
    rooms = Room.objects.all()
    return render(request, "all_rooms.html", {'rooms': rooms, "title": "hello this title comes from django"})  # render(request, "템플릿명.html", {템플릿에 넘겨줄 변수: 값})


def see_one_room(request, room_id):
    try:
        room = Room.objects.get(id=room_id) # If there is matched 'room_id', render 'room_detail.html' template with 'room' data
        return render(request, "room_detail.html", {"room": room} )
    
    except Room.DoesNotExist:# If there is no matched 'room_id', render 'room_detail.html' template with 'not_found' data
        return render(request, "room_detail.html", {'not_found': True})
    
