from journal.models import Journal
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']


class JournalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		user = UserSerializer()
		model = Journal
		fields = '__all__'
