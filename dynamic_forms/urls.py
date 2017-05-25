from django.conf.urls import url
from . import views

urlpatterns = [
    # forms/2
    url(r'^(?P<pk>\d+)/$', views.show_form, name='show_form'),
]