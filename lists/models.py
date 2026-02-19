from django.db import models

class List(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    movies = models.ManyToManyField('movies.Movie', related_name='lists')

    def __str__(self):
        return self.name
