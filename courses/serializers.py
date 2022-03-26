from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from courses.models import *


class CoursesSerializer(ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'

