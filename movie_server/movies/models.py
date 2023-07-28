from django.db import models
import uuid

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=50, blank=True)
class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    db_id = models.IntegerField(default=None)
    genre_ids = models.ManyToManyField(Genre)
    title = models.CharField(max_length=50, null=True, blank=True)
    overview = models.CharField(max_length=250, null=True, blank=True)
    poster_path = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.CharField(max_length=100, null=True, blank=True)
    original_title = models.CharField(max_length=50, null=True, blank=True)
    original_language = models.CharField(max_length=50, null=True, blank=True)

