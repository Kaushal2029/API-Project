from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from .models import *


class BookApiView(APIView):
    serializer_class = BookSerializers
    def get(self,request):
        allBooks = Book.objects.all().values()
        return Response({'message':"list of books","book list":allBooks})
    def post(self,request):
        print("Request Data is : ",request.data)
        serializer_obj = BookSerializers(data = request.data)
        if(serializer_obj.is_valid()):
            Book.objects.create(
                id = serializer_obj.data.get("id"),
                title = serializer_obj.data.get("title"),                             
                author = serializer_obj.data.get("author"),                             
                                )
        Books = Book.objects.filter(id=request.data["id"]).values()
        return Response({'message':"new book added","book":Books})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

# Create your views here.
def home(request):
    return render(request,"home.html")
