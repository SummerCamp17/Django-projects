from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^$', views.index, name="index"),
]