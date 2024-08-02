from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import ChoiceField

from main_app.managers import DirectorManager


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )
    birth_date = models.DateField(
        default='1900-01-01',
    )
    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )


class Director(BaseModel):
    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )

    objects = DirectorManager()


class Actor(BaseModel):
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)


class GenreChoices(models.TextChoices):
    Action = "Action", "Action"
    Comedy = "Comedy", "Comedy"
    Drama = "Drama", "Drama"
    Other = "Other", "Other"


class Movie(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)],
    )
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(
        choices=GenreChoices.choices,
        max_length=6,
        default=GenreChoices.Other
    )
    rating = models.DecimalField(
        max_digits=3,decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(to=Actor, on_delete=models.SET_NULL,  related_name='starring_movies', blank=True, null=True)
    actors = models.ManyToManyField(to=Actor, related_name='actors_movies')
