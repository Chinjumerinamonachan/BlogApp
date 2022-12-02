from rest_framework import serializers
from django.contrib.auth import get_user_model

USER = get_user_model()
  
class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ["username", "password","email","first_name","last_name","date_of_birth","Phone_no"]