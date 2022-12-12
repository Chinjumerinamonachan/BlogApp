import json
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate,logout
from blog_api.serializers import ArticleSerializer, UserSerializer,ArticleUpdateSerializer,ArticleListSerializer,ArticleCommentListSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
USER = get_user_model()
from myblog.models import Article,Comment


# @api_view(['POST'])
# def login_user(request):
#     serializer = UserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
    
#     return Response({
#         'user_data': {user.id,
#         user.username}
#     })

# the api for login
@api_view(['POST'])
# @authentication_classes([]) 
# @permission_classes([AllowAny,]) 
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
            token, _ = Token.objects.get_or_create(user=user)
            data={
                
                "user_id":request.user.pk,
                "username":request.user.username,
                "token": token.key
        }
            return Response({"success":"successfully login","data":data}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid user can not login"}, status=status.HTTP_400_BAD_REQUEST)


#the api for logout

@api_view(['POST'])
# @authentication_classes([]) 
# @permission_classes([])
def logout_user(request):
    if request.method =='POST':
        username = request.data.get('username')
        check_user=USER.objects.filter(username=username).exists()
        if check_user== False:
            return Response({"error":"the user is not exists"})
        user=authenticate(username=username)
        if user is not None: 
            logout(request,user)
            
        return Response('User Logged out successfully')
    
# the api for listing article

@api_view(['GET'])
@authentication_classes([]) 
@permission_classes([])
def article_list(request,id):
    if request.method == "GET":
        userid=USER.objects.get(pk=id)
        print("................................",userid)
        articles = Article.objects.filter(author=userid)
        print(articles)
        serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

# the api for view comment 

@api_view(['GET'])
@authentication_classes([]) 
@permission_classes([]) 
def article_comment_and_like_list(request,id):
    if request.method == "GET":
        article_id=Article.objects.get(pk=id)
        print("................................",article_id)
        comments = Comment.objects.filter(post=article_id)
        print(comments)
        serializer = ArticleCommentListSerializer(comments, many=True)
    return Response(serializer.data)

# the api for article/post creation

@api_view(['POST'])
@authentication_classes([]) 
@permission_classes([]) 
# @csrf_protect
def article_create(request):
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data)


#the api for article/post details

@api_view(['PUT'])
@authentication_classes([]) 
@permission_classes([]) 
# @csrf_protect
def article_detail(request,id):

   if request.method == 'PUT':
        article = Article.objects.get(pk=id) 
        serializer = ArticleUpdateSerializer(article, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
@api_view(['POST'])
@authentication_classes([]) 
@permission_classes([])
def user_post_param(request):
    if request.method =='POST':
        username=request.data.get('username')
        print(username)
        return Response({"success":"the typed username is","username":username},status=status.HTTP_200_OK)
        

@api_view(['GET'])
@authentication_classes([]) 
@permission_classes([])
def user_list_param(request):
    if request.method =='GET':
        data={}
        username=request.data.get('username')
        print(username)
        check_user=USER.objects.filter(username=username).exists()
        if check_user== False:
            return Response({"error":"the user is not exists"})
        user=USER.objects.get(username=username)
      
        data={
                
                "user_id":user.pk,
                "username":user.username,
                "email":user.email,
                 "first_name":user.first_name,
                  "last_name":user.last_name,
                   "date_of_birth":user.date_of_birth,
                   "Phone_no":user.Phone_no
                
        }
        return Response({"sucess":"Typed user is","data":data}, status=status.HTTP_200_OK)
    
        