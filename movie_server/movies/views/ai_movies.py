from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings
import requests

class AIMoviesViewSet(ViewSet):
    def create(self, request) -> JsonResponse:
        print('here')
        suggestions = requests.post(
            'http://127.0.0.1:8000/movie/suggestion/', 
            json={
                'user_input': request.data['user_input'],
                'top_k': request.data['top_k']
            }
        )
        print('here',suggestions)
        tmdb_return_dict = {}
        for _, movie_name in suggestions.json().items():
            tmdb_return = requests.get(
                f'https://api.themoviedb.org/3/search/movie?query={movie_name}',
                headers = {
                    'accept': 'application/json',
                    'Authorization': f'Bearer {settings.TMDB_TOKEN}'
                }
            )
            print('-->', tmdb_return.json())
            tmdb_return_dict[movie_name] = [
                element for element in tmdb_return.json()['results'] 
                    if movie_name.lower()==element['original_title'].lower() 
            ]
            return Response(tmdb_return_dict)