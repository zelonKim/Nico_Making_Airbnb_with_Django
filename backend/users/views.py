import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from . import serializers 
from .models import User 


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)


    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data = request.data,
            partial = True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

###################

class Users(APIView):
    def post(self, request):
        password = request.data.get('password')
        if not password: 
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)  # 'set_password()' hashes the given password
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
###################

class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
    
###################

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not old_password or not new_password:
           raise ParseError
        
        if user.check_password(old_password): # 'check_password()' returns True If the given password is correct
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError
        
###################

class LogIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password,) # 'authenticate(request, username=유저명, password=비밀번호)' returns the 유저 데이터 that matches the given username and password
        
        if user:
            login(request, user) # 'login(request, 유저 데이터)' logins the user with creating session and giving cookie to the user
            return Response({"ok":"Welcome"})
        else:
            return Response({"error":"wrong password"})

###################

class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request) # 'logout(request)' logouts
        return Response({"ok": "bye"})
    






########################








class JWTLogIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password,)

        if user:
            token = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
            return Response({'token': token})
        else:
            return Response({"error":"wrong password"})