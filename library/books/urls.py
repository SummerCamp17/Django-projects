from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^$', views.index, name="index"),
]