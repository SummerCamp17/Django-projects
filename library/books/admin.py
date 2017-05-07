from django.contrib import admin
from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status')

    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author')
        }),
        ('Availability', {
            'fields': ('quantity', 'status')
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.register(Author)
