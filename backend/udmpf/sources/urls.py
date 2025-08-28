from django.urls import path

from sources.views import SourcesListView


app_name = 'sources'

urlpatterns = [
    path('', SourcesListView.as_view(), name='index'),
]
