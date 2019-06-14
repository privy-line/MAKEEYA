from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),  
    url(r'^profile/(\d+)',views.profile,name ='profile'),
    url(r'^profiles/(\d+)',views.myProfile,name ='MyProfile'),
    url(r'^request/$', views.post_request, name='post_request'),
    url(r'^create_item/',views.create_item,name='create_item'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)