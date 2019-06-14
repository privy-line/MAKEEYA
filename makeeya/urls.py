from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'), 
 
    url(r'^profile/(\d+)',views.profile,name ='profile'),
    url(r'^request/$', views.post_request, name='post_request')
]