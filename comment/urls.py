from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns = [
  url(r'^$',views.comment,name='comment'),
]
