from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    # # this is the method responsible for insertion of data with hashed password
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)