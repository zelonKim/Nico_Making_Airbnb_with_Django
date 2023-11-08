""" 
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
"""
    


from rest_framework.views import APIView
from .models import Amenity
from .serializers import AmenitySerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(AmenitySerializer(amenity).data,)
        else:
            return Response(serializer.errors)



class AmenitiyDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True,)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else: 
            return Response(serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)
