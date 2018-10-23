from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
handler404 = 'my_app.views.handler404'
handler500 = 'my_app.views.handler500'
handler401 = 'my_app.views.handler401'
handler400 = 'my_app.views.handler400'