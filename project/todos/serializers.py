from rest_framework import serializers
from .models import Todo

#creating serializer for todo app showing all fields to the user.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"