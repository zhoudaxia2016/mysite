from django.conf.urls import url
from . import views

app_name = 'word'
urlpatterns = [
  url(r'^leave/?$',views.leave,name='leave'),
  url(r'^$',views.word,name='word'),
]
