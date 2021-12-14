from makers.serializers import ApplicationSerializer
from rest_framework import serializers
from .models import User


# from .models import User
class UserSerializer(serializers.ModelSerializer):
	# email = seria
	applications = ApplicationSerializer(many=True, read_only=True)
	class Meta:
		model = User
		exclude = ('is_superuser','is_active', 'user_permissions')
		extra_kwargs = {"password" : {"write_only" : True}}
	
	def create(self, validated_data):
		user = User.objects.create(username = validated_data['username'], email = validated_data['email'], password=validated_data['password'])
		return user
