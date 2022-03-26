from django.shortcuts import render
from rest_framework import  filters
from courses.serializers import CoursesSerializer
from courses.models import *
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class CoursesAPIView(ListCreateAPIView):
    serializer_class = CoursesSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Courses.objects.filter()

class CoursesDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CoursesSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Courses.objects.filter()
