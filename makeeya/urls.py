from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),  
    url(r'^profile/(\d+)',views.profile,name ='profile'),
    url(r'^myProfile/(\d+)',views.myProfile,name ='myProfile'),
    url(r'^request/$', views.post_request, name='post_request'),
    url(r'^create_item/',views.create_item,name='create_item'),
]
 

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
 
 
 
