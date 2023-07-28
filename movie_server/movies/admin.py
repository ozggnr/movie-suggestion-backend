from django.contrib import admin
from movie_server.movies.models import Movie, Genre
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
