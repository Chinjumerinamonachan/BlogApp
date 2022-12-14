from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views import generic as views
from django.conf import settings
from django.contrib.auth import get_user_model
from user.forms import UserLoginForm, CustomUserRegistrationForm
from django.contrib.auth import authenticate,login
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from user.models import CustomUser
from user.serializers import UserViewSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser 

USER = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password,email=user.email)

           
            return redirect('myblog:home')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_page(request):
    form = form.UserLoginForm()
    # message = ''
    if request.method == 'POST':
        form = form.UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

        if user is not None:
                login(request, user)
           
        else:
            form = UserLoginForm()
            
    return render(request, 'registration/login.html', context={'form': form})

@api_view(['GET'])
@permission_classes([]) 
def Userview(request):
    print("--------------------- 1 -----------------------")
    if request.method == 'GET':
        print("--------------------- 2 -----------------------")
        users = USER.objects.all()
        print("--------------------- 3 -----------------------")
        print(users)
        print("--------------------- 4 -----------------------")
        serializer = UserViewSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([]) 
def post_Userdata(request):
    if request.method == 'POST':
        serializer = UserViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([]) 
def post_userdetail(request,id):
    try: 
        user = USER.objects.get(pk=id) 
    except USER.DoesNotExist: 
        return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
   
 
    if request.method == 'PUT':
        # user_data = JSONParser().parse(request) 
        # print(".................",user_data)
        serializer = UserViewSerializer(user, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
        

      




    

