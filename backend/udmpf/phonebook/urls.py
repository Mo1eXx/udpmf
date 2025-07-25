from django.urls import include, path

from rest_framework import routers

from .views import (
    #KontaktListView,
    #KontaktViewSet
    index
)


app_name = 'phonebook'

# router = routers.DefaultRouter()
#
# router.register('kontakts', KontaktViewSet, basename='kontakts')

urlpatterns = [
    path('', index, name='index')
    #path('', KontaktListView.as_view(), name='index')
    #path('', include(router.urls))
]
