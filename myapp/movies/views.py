from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
from django.views.generic.list import ListView
from django.core.paginator import Paginator

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type='action')
    serializer_class = MovieSerializer

class MovieList(ListView):
    model = MovieData
    template_name = 'movies/movie_list.html'
    context_object_name = 'movie_list'
    paginate_by = 2
    
    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('search')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset
    