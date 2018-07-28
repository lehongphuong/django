from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'/', views.home),
    url(r'header', views.header),
    url(r'menu', views.menu), 
]
