from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
  url(r'^signup/?$',views.signup,name='signup'),
  url(r'^signin/?$',views.signin,name='signin'),
  url(r'^logout/?$',views.logout,name='logout'),
  url(r'^$',views.login,name='login'),
]
