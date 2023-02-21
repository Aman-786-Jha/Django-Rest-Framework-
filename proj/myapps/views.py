from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer, RegisterSerializer

class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['work_type']
    search_fields = ['artist__name']

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    search_fields = ['name']

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

