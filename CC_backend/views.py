from CC_backend.serialization import *
from CC_backend.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
import json
# from django.contrib.auth.models import user, auth

@api_view(['POST'])
def signup(request):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('saved data')

@api_view(['POST'])
def signin(request):
    if request.method=='POST':
        jsonResponse = json.loads(request.body.decode('utf-8'))
        usern = jsonResponse['email']
        passw = jsonResponse['password']
        result = display_users.objects.get(email=usern)
        serialize = display_users_serialization(result, many=False)
        if(passw==result.password):
            print(result)
            return Response(serialize.data)
        else:
            return Response('password incorrect')
    else:
        return Response('error')


@api_view(['GET'])
def show(request):
    if request.method == 'GET':
        result = testdata.objects.all()
        serialize = serializationclass(result, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def single_post(request,pid):
    if request.method == 'GET':
        result = displaypost.objects.filter(id=pid)
        serialize = upostSerializer(result, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def users(request,uid):
    if request.method == 'GET':
        result = display_users.objects.filter(id=uid)
        serialize = display_users_serialization(result, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def user_post(request):
    if request.method == 'GET':
        result = displaypost.objects.all()
        serialize = upostSerializer(result, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def add_post(request):
    serializer = addpostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('post added')

@api_view(['GET'])
def user_details(request, uid):
    result = displaypost.objects.filter(user_id=uid)
    serialize = upostSerializer(result, many=True)
    return Response(serialize.data)
    #do something with this user


@api_view(['GET'])
def ratings(request, uid):
    result = user_rating.objects.filter(user_id=uid)
    serialize = ratingsserialization(result, many=True)
    return Response(serialize.data)