from CC_backend.serialization import *
from CC_backend.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from operator import attrgetter
from itertools import chain
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
        result = login.objects.get(email=usern)
        serialize = user_login(result, many=False)
        if(passw==result.password):
            print(result)
            return Response(serialize.data)
        else:
            return Response('password incorrect')
    else:
        return Response('error')

@api_view(['GET'])
def show_type(request):
    if request.method == 'GET':
        result = user_type.objects.all()
        serialize = user_type_serialization(result, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def show_cart(request,uid):
    if request.method == 'GET':
        result = cart_data.objects.raw('select * from posts, cart,type where posts.post_type=type.id and posts.id=cart.post_id and cart.user_id='+uid)
        serialize = viewcartSerializer(result, many=True)
        return Response(serialize.data)

@api_view(['POST'])
def add_cart(request):
    serializer = addcartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
    return Response('Added to cart')

@api_view(['GET'])
def single_post(request,pid):
    if request.method == 'GET':
        result = singlepost.objects.raw('select * from users, posts where posts.user_id=users.id and posts.id='+pid)
        serialize = viewsingleSerializer(result, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def users(request,uid):
    if request.method == 'GET':
        result = display_users.objects.raw('select * from users,type where users.user_type=type.id and users.id='+uid)
        serialize = display_users_serialization(result, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def user_post(request,type):
    if request.method == 'GET':
        result = displaypost.objects.filter(post_type=type)
        serialize = upostSerializer(result, many=True)
        return Response(serialize.data)

@api_view(['POST'])
def add_post(request):
    serializer = addpostSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        obj = displaypost.objects.latest('id')
        t = displaypost.objects.get(id=obj.id)
        t.post_price = 999  # send data from file 
        t.save()
        return Response('post added')
    else:
        return Response('not saved')

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

@api_view(['GET'])
def get_orders(request,pid):
    if request.method == 'GET':
        result = orders.objects.raw('select * from posts,orders where orders.pid=posts.id and orders.uid='+pid)
        serialize = vieworders(result, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def get_orders_byseller(request,pid):
    if request.method == 'GET':
        result = orders.objects.raw('select * from posts,orders where orders.pid=posts.id and orders.pid='+pid)
        serialize = vieworders(result, many=True)
        return Response(serialize.data)

@api_view(['POST'])
def add_orders(request):
    serializer = add_order_serializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('order added')
    else:
        return Response('not saved')

@api_view(['PUT'])
def ratings_update(request, uid):
    result = user_rating.objects.get(user_id=uid)
    data = request.data
    if(data['rating']==5):
        result.star5 = result.star5+1
        result.save()
    elif(data['rating']==4):
        result.star4 = result.star4+1
        result.save()
    elif(data['rating']==3):
        result.star3 = result.star3+1
        result.save()
    elif(data['rating']==2):
        result.star2 = result.star2+1
        result.save()
    elif(data['rating']==1):
        result.star1= result.star1+1
        result.save()
    
    result = orders.objects.get(id=1)
    result.review = 1
    result.save()
    return Response('response saved')

@api_view(['GET'])
def top_users(request):
    if request.method == 'GET':
        result = display_users.objects.raw('SELECT * from users ORDER by rating DESC')
        serialize = display_users_serialization(result, many=True)
        return Response(serialize.data)

@api_view(['GET'])
def view_wallet(request, uid):
    if request.method == 'GET':
        result = user_wallet.objects.filter(uid=uid)
        serialize = get_wallet(result, many=True)
        return Response(serialize.data)
