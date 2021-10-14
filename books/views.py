from django.shortcuts import render
from books.serializer import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class BooksOperations(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer