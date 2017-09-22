__author__ = 'Nithin'

from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^submit', views.submit),
    url(r'^take_review', views.take_review),
    url(r'^takereviewtwo', views.takereviewtwo)

]
