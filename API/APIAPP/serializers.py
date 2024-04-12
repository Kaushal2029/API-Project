from rest_framework import serializers
from .models import *

class BookSerializers(serializers.Serializer):
    id = serializers.IntegerField(label="Enter Book ID")
    title = serializers.CharField(label="Enter Book Title")
    author = serializers.CharField(label="Enter Author")

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"