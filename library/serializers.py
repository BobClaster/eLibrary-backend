from rest_framework import serializers
from library.models import Book, Author, TakeBook
from user_app.serializers import StudentSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class ListBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['barcode', 'title', 'author']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['barcode', 'title', 'author', 'description']


class TakeBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    student = StudentSerializer()

    class Meta:
        model = TakeBook
        fields = ['book', 'student', 'take_date']


class StudentBooksSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = TakeBook
        fields = ['book', 'take_date', 'returned', 'returned_date']
