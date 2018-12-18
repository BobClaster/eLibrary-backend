from django.contrib import admin
from user_app.models import Student, Group, Faculty, Librarian

admin.site.register(Librarian)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Faculty)
