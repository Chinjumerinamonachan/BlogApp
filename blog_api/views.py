import json
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate,logout
from blog_api.serializers import ArticleSerializer, UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import requires_csrf_token
USER = get_user_model()
from myblog.models import Article


# @api_view(['POST'])
# def login_user(request):
#     serializer = UserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
    
#     return Response({
#         'user_data': {user.id,
#         user.username}
#     })
@api_view(['POST'])
@authentication_classes([]) 
@permission_classes([]) 
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password= request.data.get('password')

        if not username or not password:
            return Response ({"error":"please mention all fields"})
        check_user=USER.objects.filter(username=username).exists()
        if check_user== False:
            return Response({"error":"the user is not exists"})
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            
            data={
                
                "user_id":request.user.pk,
                "username":request.user.username
        }
            return Response({"success":"successfully login","data":data}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid user can not login"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([]) 
@permission_classes([]) 
def logout_user(request):
    if request.method =='GET':
        username = request.data.get('username')
        check_user=USER.objects.filter(username=username).exists()
        if check_user== False:
            return Response({"error":"the user is not exists"})
        user=authenticate(username=username)
        if user is not None: 
            logout(request,user)
            
        return Response('User Logged out successfully')


@api_view(['POST'])
@permission_classes([])
def article_create(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([]) 
def article_detail(request,id):
   if request.method == 'PUT':
        user = USER.objects.get(pk=id) 
        serializer = ArticleSerializer(user, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
