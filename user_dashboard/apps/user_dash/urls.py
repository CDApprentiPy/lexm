from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^register$', views.register),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/admin$', views.dash_admin),
    url(r'^users/new$', views.new_user),
    url(r'^users/edit$', views.user_edit),
    url(r'^users/edit/(?P<id>\d+)$', views.user_edit_admin),
    url(r'^users/show/(?P<id>\d+)$', views.show_user),
    url(r'^users/delete/(?P<id>\d+)$', views.user_delete),
    url(r'^update$', views.update),
    url(r'^change_pass$', views.change_pass),
    url(r'^edit_desc$', views.edit_desc),
    # url(r'^show_user$', views.show_user),
]
