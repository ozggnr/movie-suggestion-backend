from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict
import requests
from movie_server.movies.models import Genre, Movie
from movie_server.movies.serializer import MovieSerializer

class AIMoviesViewSet(ViewSet):
    def create(self, request) -> JsonResponse:

        suggestions = requests.post(
            'http://127.0.0.1:8000/movie/ai/suggestion/', 
            json={
                'user_input': request.data['user_input'],
                'top_k': request.data['top_k']
            }
        )
        
        movie_list = {}
        for _, movie_name in suggestions.json().items():
            try:
                movie = Movie.objects.get(title=movie_name.lower())
                serializer = MovieSerializer(movie)
                movie_list[str(movie.id)] = serializer.data
                # print('in-try-->', movie_list)
            except Movie.DoesNotExist:
                response = requests.get(
                    f'https://api.themoviedb.org/3/search/movie?query={movie_name}',
                    headers = {
                        'accept': 'application/json',
                        'Authorization': f'Bearer {settings.TMDB_TOKEN}'
                    }
                )
                movies = response.json()['results']
                matched_movies = [
                    movie for movie in movies
                        if movie_name.lower() == movie['original_title'].lower()
                ]
                if matched_movies:
                    matched_movie = sorted(
                        matched_movies,
                        key=lambda x: x['vote_count'], 
                        reverse=True
                    )[0]
                    # print('matched movie', matched_movie, matched_movie['genre_ids'])
                    #[80, 18]
                    genres = Genre.objects.filter(code__in=matched_movie['genre_ids'])   
                                    
                    movie = Movie(
                        title=matched_movie['title'].lower(),
                        db_id=matched_movie['id'],
                        overview=matched_movie['overview'],
                        poster_path=matched_movie['poster_path'],
                        release_date=matched_movie['release_date'],
                        original_title=matched_movie['original_title'],
                        original_language=matched_movie['original_language']
                    )
                    movie.save()
                    movie.genre_ids.add(*genres)
                    serializer = MovieSerializer(movie)
                    movie_list[str(movie.id)] = serializer.data
                    # print('in except', movie_list)
                else:
                    continue


        return Response(movie_list)
