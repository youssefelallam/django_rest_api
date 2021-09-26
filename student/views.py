from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Filier,Students


class FilierList(generics.ListCreateAPIView):
    queryset = Filier.objects.all()
    serializer_class = FilierSerializers

class FilierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filier.objects.all()
    serializer_class = FilierSerializers

class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers

class StudentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers