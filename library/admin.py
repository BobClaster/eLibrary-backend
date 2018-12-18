from django.contrib import admin
from library.models import Book, Author, TakeBook

admin.site.register(Book)
admin.site.register(Author)


# class TakeBookAdmin(admin.ModelAdmin):
    # list_display = ['book', 'student', 'librarian', 'take_date', 'returned', 'returned_date']
admin.site.register(TakeBook)
