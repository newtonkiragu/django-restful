from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet'),
]
handler404 = 'my_app.views.handler404'
handler500 = 'my_app.views.handler500'
handler401 = 'my_app.views.handler401'
handler400 = 'my_app.views.handler400'