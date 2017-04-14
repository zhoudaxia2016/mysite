from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index\.html/?$',views.index,name='index'),
    url(r'^blog/?$',views.blog,name='blog'),
    url(r'^demo/?$',views.demo,name='demo'),
    url(r'^about/?$',views.about,name='about'),
    url(r'^event/?$',views.event,name='event'),
    url(r'^detail/(\d+)$',views.detail,name='detail'),
    url(r'^$',views.index,name='index'),
]
