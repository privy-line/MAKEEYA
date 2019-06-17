from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'), 
 
    url(r'^profile/(\d+)',views.profile,name ='profile'),
    url(r'^profiles/(\d+)',views.myProfile,name ='myProfile'),
    url(r'^request/$', views.post_request, name='post_request'),
    url(r'^create_item/(\d+)', views.create_item, name='create_item'),
    url(r'^last_day_items/$', views.last_day, name='last_day'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
 
 
 