from courses.views import *
from django.urls import path

urlpatterns = [
    path('', CoursesAPIView.as_view(), name='courses'),
    path('<int:id>', CoursesDetailAPIView.as_view(), name='course')
]
