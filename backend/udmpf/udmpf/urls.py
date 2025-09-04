from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('phonebook.urls', namespace='phonebook')),
    path('contest/', include('contest.urls', namespace='contest')),
    path('sources/', include('sources.urls', namespace='sources')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('userProfile/', include('userProfile.urls', namespace='userProfile'))
]

handler404 = 'core.views.page_not_found'
