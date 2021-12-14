from django.db.models.base import Model
from rest_framework import serializers
from .models import Group, Application

class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Application
		fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
	applications = ApplicationSerializer(many=True, read_only=True)
	class Meta:
		model = Group
		fields = '__all__'

