from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^api/v2/snippets/$', views.snippet_list),
    url(r'^api/v2/snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
