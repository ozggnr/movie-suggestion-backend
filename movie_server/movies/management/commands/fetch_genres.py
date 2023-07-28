from django.core.management.base import BaseCommand
from django.conf import settings
from movie_server.movies.models import Genre
import requests

class Command(BaseCommand):
    help = 'Fetch genres from TMDB and save them to the database'

    def handle(self, *args, **options):
        response = requests.get('https://api.themoviedb.org/3/genre/movie/list', headers={
            'Authorization': f'Bearer {settings.TMDB_TOKEN}',
            'Content-Type': 'application/json;charset=utf-8',
        })
        tmdb_genres = response.json()['genres']
        print(tmdb_genres)
        for genre in tmdb_genres:
            Genre.objects.get_or_create(code=genre['id'], defaults={'name': genre['name']})

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved genres'))
