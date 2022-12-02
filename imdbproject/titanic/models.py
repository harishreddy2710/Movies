from django.db import models


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=50)
    rating = models.CharField(max_length=50, default=1)
    director = models.CharField(max_length=100)
    storyline = models.TextField()
    genre = models.TextField()
    top_cast = models.TextField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.movie_name

# Create your models here.
