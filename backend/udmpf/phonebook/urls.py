from django.urls import path

from .views import PhonebookListView


app_name = 'phonebook'


urlpatterns = [
    path('', PhonebookListView.as_view(), name='index'),
]
