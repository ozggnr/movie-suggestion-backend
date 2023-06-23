from rest_framework.decorators import api_view
# from rest_framework.response import JsonResponse
from django.http import JsonResponse
from os import getenv
import requests
import dotenv
import requests

dotenv.load_dotenv()
BEAR_TOKEN = getenv('BEAR_TOKEN')

api_view(['GET'])
def get_popular_movies(request):
    print('BEAR: ', BEAR_TOKEN)
    url = 'https://api.themoviedb.org/3/movie/popular'
    headers = {
        'Authorization': f'Bearer {BEAR_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return JsonResponse(response.json())