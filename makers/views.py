from django.shortcuts import get_object_or_404, render
from account import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import GroupSerializer
from .models import Application, Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, api_view, permission_classes

# Create your views here.
class GroupView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request:Request):
		serializer = GroupSerializer(data=request.data)
		if serializer.is_valid():
			group = serializer.save()
			application = Application()
			application.applicant = request.user
			application.group = group
			application.postion = application.ADMIN
			application.save()
			return Response(GroupSerializer(group).data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetailView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request:Request, pk:int):
		group = get_object_or_404(Group, pk=pk)
		serializer = GroupSerializer(group)
		return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def join_group(request:Request, pk:int):
	group = get_object_or_404(Group, pk=pk)
	application = Application()
	application.applicant = request.user
	application.group = group
	application.save()
	return Response(GroupSerializer(group).data)
