from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.movies import get_popular_movies
from .views.ai_movies import AIMoviesViewSet

router = DefaultRouter()
# router.register(r'', movies.get_popular_movies, name='movie-list')
router.register(r'ai', AIMoviesViewSet, basename='ai-movies')


urlpatterns = [
    path('',  get_popular_movies, name='movie-list')
] + router.urls
