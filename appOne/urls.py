from django.conf.urls import url
from appOne import  views

urlpatterns = [
    url(r'',views.viewers,name='users'),
]