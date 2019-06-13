from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'), 
    url(r'^request/$', views.post_request, name='post_request')
]