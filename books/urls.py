from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^authors/(?P<author_id>[0-9])/delete', views.destroy, name="author_delete"),
  url(r'^authors/new', views.new, name="author_new"),
  url(r'^authors/create', views.create, name="author_create"),
  url(r'^authors/(?P<author_id>[0-9])/show', views.show, name='author_detail'),
  url(r'^authors/(?P<author_id>[0-9])/edit', views.edit, name='auhthor_edit'),
  url(r'^authors/(?P<author_id>[0-9])/update', views.update, name='author_update'),
]
