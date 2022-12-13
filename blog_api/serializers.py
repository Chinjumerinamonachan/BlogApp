from rest_framework import serializers,validators
from django.contrib.auth import get_user_model
from myblog.models import Article,Comment
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
        fields = ["title","author", "content","status"]

class ArticleUpdateSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, max_length=100)
    # content=serializers.CharField(required=True, max_length=100)
    class Meta:
        model=Article
        fields = ["id","title", "content"]

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id","title","author", "content","created_on","updated_on","status","likes"]

class ArticleCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "body","created","updated","active"]

class UsersignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ["username", "password","email","first_name","last_name","date_of_birth","Phone_no"]





