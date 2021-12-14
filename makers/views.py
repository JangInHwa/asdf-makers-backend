from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import GroupSerializer
from .models import Application
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class Group(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def post(self, request:Request):
		serializer = GroupSerializer(data=request.data)
		if serializer.is_valid():
			group = serializer.save()
			application = Application()
			application.applicant = request.user
			application.group = group
			application.save()
			return Response(GroupSerializer(group).data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
