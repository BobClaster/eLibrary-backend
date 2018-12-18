from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics

from datetime import datetime

from .models import Book, TakeBook, Student
from .serializers import ListBookSerializer, BookSerializer, TakeBookSerializer, StudentBooksSerializer


class ListBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer


class SingleBookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TakeBookView(generics.GenericAPIView):
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializer

    def post(self, request, *args, **kwargs):
        barcode = request.data.get("barcode")
        student_id = request.data.get("student_id")
        try:
            exist_take_book = TakeBook.objects.filter(
                book__barcode=barcode, student__student_id=student_id, returned=False
            )
            if exist_take_book:
                exist_take_book = exist_take_book[0]
                exist_take_book.returned = True
                exist_take_book.returned_date = datetime.now()
                exist_take_book.save()
                return Response(TakeBookSerializer(exist_take_book).data)

            book = Book.objects.get(pk=barcode)
            student = Student.objects.get(student_id=student_id)
            take_book = TakeBook(book=book, student=student)
            take_book.save()
            return Response(TakeBookSerializer(take_book).data)

        except Book.DoesNotExist:
            return Response(
                data={
                    "message": f"Book with barcode: {request.data.get('barcode')} does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BooksUserProfileView(generics.ListAPIView):
    serializer_class = StudentBooksSerializer
    model = TakeBook

    def get_queryset(self):
        student_id = self.kwargs["student_id"]
        return self.model.objects.filter(student__student_id=student_id).order_by("returned")
