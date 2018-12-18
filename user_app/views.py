from rest_framework import generics, mixins
from rest_framework.response import Response

from .models import Student
from .serializers import ListStudentSerializer, StudentSerializer
from library.models import TakeBook


class ListUserProfileView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer


class UserProfileView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'
