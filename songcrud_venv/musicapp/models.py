from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.DateTimeField('date published')

class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField('date published')
    likes = models.IntegerField( )
    artise_id = models.CharField(max_length=200)

class Lyric(models.Model):
    content = models.CharField(max_length=200)
    song_id = models.CharField(max_length=200)
