from django.conf.urls import url, include
from . import views

app_name = 'restaurent'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^success', views.success, name='success'),
]
