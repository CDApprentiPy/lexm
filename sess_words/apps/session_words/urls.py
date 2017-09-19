from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.main),
    url(r'^addword$', views.addword),
    url(r'^clear$', views.clear),
]
