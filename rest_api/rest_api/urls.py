from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.contrib import admin
from stock_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stock/', views.StockView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)