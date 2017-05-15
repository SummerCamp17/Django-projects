from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'borrower')
    list_filter = ('status', 'borrower')

    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author')
        }),
        ('Availability', {
            'fields': ('status', 'borrower')
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.register(Author)
