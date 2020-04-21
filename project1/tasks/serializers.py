from tasks.models import Tasks, TaskCategory
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		user = UserSerializer()
		model = Tasks
		fields = '__all__'


class TaskCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TaskCategory
		fields = '__all__'
