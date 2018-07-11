from django.conf.urls import url
from . import views   


urlpatterns = [
  url(r'^users$', views.users)  ,
  url(r'^users/new$', views.new),
  url(r'^users/create$', views.create),
  url(r'^users/(?P<id>\d+)/show$', views.show),
  url(r'^users/(?P<id>\d+)/edit$', views.update),
  url(r'^users/(?P<id>\d+)/delete$', views.delete)
  url(r'^users/destroy$', views.destroy)
]