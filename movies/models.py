from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        HORROR = 'Horror', 'Horror'
        SCI_FI = 'Sci-Fi', 'Sci-Fi'
        ROMANCE = 'Romance', 'Romance'
        THRILLER = 'Thriller', 'Thriller'
        FANTASY = 'Fantasy', 'Fantasy'
        ANIMATION = 'Animation', 'Animation'
        DOCUMENTARY = 'Documentary', 'Documentary'
        CRIME = 'Crime', 'Crime'
        ADVENTURE = 'Adventure', 'Adventure'
        MYSTERY = 'Mystery', 'Mystery'
        FAMILY = 'Family', 'Family'
        HISTORY = 'History', 'History'
        MUSIC = 'Music', 'Music'
        WAR = 'War', 'War'
        WESTERN = 'Western', 'Western'

    title = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(1)
        ]
    )
    tagline = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    description = models.TextField(
        null=True,
        blank=True)
    release_date = models.DateField()
    genre = models.CharField(
        max_length=20,
        choices=Genre.choices)
    image_url = models.URLField()
    slug = models.SlugField(unique=True, editable=False)
    runtime = models.IntegerField()
    director = models.ForeignKey('directors.Director', on_delete=models.CASCADE, related_name='movies')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.release_date.year}")
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title + ' ' + str(self.release_date.year)


    class Meta:
        constraints = [models.UniqueConstraint(fields=['title', 'release_date'], name='unique_movie')]


