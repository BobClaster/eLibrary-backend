from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True, blank=True)
    dean = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=20)
    numb_of_student = models.IntegerField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.faculty}"


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.SlugField("Student ID")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
