from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updateinfo', views.updateinfo, name='updateinfo'),
    path('helpfilter', views.helpfilter, name='helpfilter'),
]
