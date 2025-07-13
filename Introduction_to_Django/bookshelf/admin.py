from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filter sidebar for easier data filtering
    list_filter = ('author', 'publication_year')

    # Enable search bar for title and author fields
    search_fields = ('title', 'author')
