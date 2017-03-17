from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^register$', views.register , name='register'),
    url(r'^updateDashboard$', views.updateDashboard , name='updateDashboard'),
    url(r'^dashboard$', views.dashboard , name='dashboard'),
    url(r'^post$', views.post , name='post'),
    url(r'^loginview$', views.loginview , name='loginview'),
    url(r'^userlogin$', views.userlogin , name='userlogin'),
    url(r'^questions$', views.questions , name='questions'),
    url(r'^reply$', views.reply , name='reply'),
    url(r'^([0-9])$', views.thread , name='thread'),
]
