from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Author


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = Book.objects.filter(status__exact=1).count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


class BookListView(generic.ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Book

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'books/book_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(borrower=self.request.user).filter(status__exact=0)

