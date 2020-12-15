from CC_backend.serialization import *
from CC_backend.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
import json
# from django.contrib.auth.models import user, auth

@api_view(['GET'])
def show(request):
    if request.method == 'GET':
        result = testdata.objects.all()
        serialize = serializationclass(result, many=True)
        return Response(serialize.data)
@api_view(['GET'])
def display(request):
    if request.method == 'GET':
        result = displaydata.objects.all()
        serialize = displayserialization(result, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def login(request):
    serializer = userSerializer(data=request.data)
    print('ok')
    if serializer.is_valid():
        serializer.save()
        print('data is: ',serializer.data)
    return Response('saved data')

def submit(request):
    print(request.POST)
    return Response(serialize.data)

@api_view(['POST'])
def signin(request):
    if request.method=='POST':
        jsonResponse = json.loads(request.body.decode('utf-8'))
        usern = jsonResponse['username']
        passw = jsonResponse['password']
        result = displaydata.objects.get(email=usern)
        serialize = displayserialization(result, many=False)
        if(passw==result.password):
            print(result)
            return Response(serialize.data)
        else:
            return Response('password incorrect h')
    else:
        return Response('error1')
        # {"username":"Aviral","password":"sharma"}