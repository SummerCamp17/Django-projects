
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^admin/', admin.site.urls),
]
