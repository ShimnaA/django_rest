from rest_framework import serializers
from .models import Actor

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name', 'alias')
