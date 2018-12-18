from rest_framework import serializers
from .models import Student, Group, Faculty, User
# from library.serializers import ListBookSerializer, TakeBook


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name', 'dean']


class GroupSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()

    class Meta:
        model = Group
        fields = ['name', 'faculty']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ListStudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_id', 'group']


class StudentSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['user', 'student_id', 'group']
        lookup_field = 'student_id'
