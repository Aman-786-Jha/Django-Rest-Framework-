from django.urls import path
from .views import WorkList, ArtistList, RegisterView

urlpatterns = [
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/artists/', ArtistList.as_view(), name='artist-list'),
    path('api/register/', RegisterView.as_view(), name='register'),
]