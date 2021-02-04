from rest_framework import serializers

from .models import *

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model=testdata
        fields='__all__'

class ratingsserialization(serializers.ModelSerializer):
    class Meta:
        model=user_rating
        fields='__all__'

class display_users_serialization(serializers.ModelSerializer):
    class Meta:
        model=display_users
        fields='__all__'


class userSerializer(serializers.ModelSerializer):
    
    name = 'aviral'
    email = 'sharma'
    password = 'somepass'
    class Meta:
        model = display_users
        fields = '__all__'

class addpostSerializer(serializers.ModelSerializer):
    
    user_id = '1'
    post_title = 'title'
    post_desc = 'desc'
    post_type = '2'
    post_price = 'price'
    class Meta:
        model = displaypost
        fields = '__all__'


class upostSerializer(serializers.ModelSerializer):
    class Meta:
        model = displaypost
        fields = '__all__'