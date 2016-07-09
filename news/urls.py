from django.conf.urls import url
from news.views import test

urlpatterns = [
    url(r'^test/$', test),
]