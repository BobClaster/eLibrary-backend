from django.urls import path
from .views import ListBooksView, SingleBookView, TakeBookView, BooksUserProfileView

urlpatterns = [
    path('', ListBooksView.as_view(), name='all_books'),
    path('<int:pk>/', SingleBookView.as_view(), name='single_books'),
    path('tb/', TakeBookView.as_view(), name='take_book'),
    path('books/<slug:student_id>/', BooksUserProfileView.as_view(), name='books_user_profile'),
]
