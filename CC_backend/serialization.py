from rest_framework import serializers

from .models import *

class user_type_serialization(serializers.ModelSerializer):
    class Meta:
        model=user_type
        fields='__all__'

class user_login(serializers.ModelSerializer):
    class Meta:
        model=login
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

class viewsingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = singlepost
        fields = '__all__'

class upostSerializer(serializers.ModelSerializer):
    class Meta:
        model = displaypost
        fields = '__all__'

class vieworders(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'

class add_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = add_order
        fields = '__all__'

class get_wallet(serializers.ModelSerializer):
    class Meta:
        model = user_wallet
        fields = '__all__'