from django.conf.urls import url
from appFour import views

app_name = 'appFour'

urlpatterns =[
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
