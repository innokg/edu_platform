"""
Standart views.py for project
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.serializers import CoursesSerializer
from courses.models import Courses


class CoursesAPIView(ListCreateAPIView):
    """Class for create and list courses"""
    serializer_class = CoursesSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Courses.objects.all()

class CoursesDetailAPIView(RetrieveUpdateDestroyAPIView):
    """Class for retrieve, udpate and delete courses"""
    serializer_class = CoursesSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Courses.objects.all()
