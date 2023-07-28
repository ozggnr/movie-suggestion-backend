from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'code', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'db_id', 'title', 'overview', 'poster_path', 'release_date', 'original_title', 'original_language', 'genre_ids']
