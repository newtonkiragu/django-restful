from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^api/v1/snippets/$', views.snippet_list),
    url(r'^api/v1/snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
