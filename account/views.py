from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['POST'])
def login(request: Request):
    if not request.data.get('email'):
        return Response('email is required',
                        status=status.HTTP_400_BAD_REQUEST)
    if not request.data.get('password'):
        return Response('password is required',
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=request.data['email'],
                        password=request.data['password'])
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'id': user.id, 'token': token.key})


@api_view(['POST'])
def register(request: Request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserSerializer(user).data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request: Request, pk: int):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)
