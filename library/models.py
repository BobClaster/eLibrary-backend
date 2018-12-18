from django.db import models
from user_app.models import Student, Librarian


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField()
    day_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    barcode = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return f"«{self.title}»  {self.author}"


class TakeBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, null=True, blank=True)
    returned = models.BooleanField(default=False)

    take_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} | {self.student} | {self.take_date}"
