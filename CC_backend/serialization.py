from rest_framework import serializers

from .models import *

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model=testdata
        fields='__all__'

class displayserialization(serializers.ModelSerializer):
    class Meta:
        model=displaydata
        fields='__all__'


class userSerializer(serializers.ModelSerializer):
    
    name = 'aviral'
    email = 'sharma'
    password = 'somepass'
    class Meta:
        model = displaydata
        fields = '__all__'