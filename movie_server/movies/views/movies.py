from rest_framework.decorators import api_view
# from rest_framework.response import JsonResponse
from django.http import JsonResponse
from django.conf import settings
import requests
import requests


api_view(['GET'])
def get_popular_movies(request):
    url = 'https://api.themoviedb.org/3/movie/popular'
    headers = {
        'Authorization': f'Bearer {settings.TMDB_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())

