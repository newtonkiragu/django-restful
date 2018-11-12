from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path
from django.conf.urls import include

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
         views.SnippetList.as_view(),
         name='snippet-list'),
    path('snippet/<int:pk>/',
         views.SnippetDetails.as_view(),
         name='snippet-detail'),
    path('snippet/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(),
         name='snippet-highlight'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('user/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
])

handler404 = 'my_app.views.handler404'
handler500 = 'my_app.views.handler500'
handler401 = 'my_app.views.handler401'
handler400 = 'my_app.views.handler400'
