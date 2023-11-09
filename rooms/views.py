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
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from django.db import transaction

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



###########################



class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)


    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():

                category_pk = request.data.get('category')
                if not category_pk:
                    raise ParseError("Category is required")
                try: 
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CatgoryKindChoices.EXPERIENCES: raise ParseError("The category`s kind should be rooms")
                except category.DoesNotExist:
                    raise ParseError("Category not found")

                try:
                    with transaction.atomic():
                        room = serializer.save(owner=request.user, category=category,)
                        amenities = request.data.get("amenities")

                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity) 

                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated





class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound    

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data) 
    
    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if room.owner != request.user:
            raise PermissionDenied
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)