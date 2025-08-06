from django.urls import path

from . import views


app_name = 'contest'


urlpatterns = [
    path('', views.ContestCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.ContestUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ContestDeleteView.as_view(), name='delete'),
]
