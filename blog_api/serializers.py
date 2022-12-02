from rest_framework import serializers,validators
from django.contrib.auth import get_user_model
from myblog.models import Article
USER = get_user_model()

  
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = USER
#         fields = ["username", "password"]
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ["username", "password","email","first_name","last_name","date_of_birth","Phone_no"]
      

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title","slug","author", "content","status"]


