from django.shortcuts import render
from django.views.generic import CreateView

from movies.forms import MovieForm
from movies.models import Movie


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm


