from django.urls import path

from .views import UserProfile

app_name = 'userProfile'

urlpatterns = [
    path('', UserProfile.as_view(), name='index')
]
