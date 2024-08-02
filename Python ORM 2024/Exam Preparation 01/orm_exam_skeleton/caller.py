import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Avg, F

from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    if (search_name is not None) and (search_nationality is not None):
        query = Director.objects.filter(full_name__icontains=search_name,
                                        nationality__icontains=search_nationality).order_by('full_name')
    elif search_name is not None:
        query = Director.objects.filter(full_name__icontains=search_name).order_by('full_name')
    else:
        query = Director.objects.filter(nationality__icontains=search_nationality).order_by('full_name')

    result = []

    if query is not None:
        result = "\n".join(
            f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}"
            for d in query
        )

    return result or ""


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    if top_director is not None:
        return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."
    else:
        return ""


def get_top_actor():
    actors = Actor.objects.prefetch_related('starring_movies').annotate(
        movies_count=Count('starring_movies'),
        average_rating=Avg('starring_movies__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not actors or not actors.movies_count:
        return ""

    movies = ", ".join(m.title for m in actors.starring_movies.all())

    return f"Top Actor: {actors.full_name}, starring in movies: {movies}, movies average rating: {actors.average_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(movies_count=Count('actors_movies')).order_by('-movies_count', 'full_name')[:3]
    if not actors or not actors[0].movies_count:
        return ''

    result = []
    for a in actors:
        result.append(f"{a.full_name}, participated in {a.movies_count} movies")

    return '\n'.join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects\
        .select_related('starring_actor')\
        .prefetch_related('actors')\
        .filter(is_awarded=True)\
        .order_by('-rating', 'title')\
        .first()

    if top_movie is None:
        return ''

    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else 'N/A'

    participating_actors = top_movie.actors.order_by('full_name').values_list('full_name', flat=True)

    cast = ', '.join(participating_actors)

    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}."\
        f" Starring actor: {starring_actor}. Cast: {cast}."


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10)

    if not movies_to_update:
        return 'No ratings increased.'

    updated_movies_count = movies_to_update.count()
    movies_to_update.update(rating=F('rating') + 0.1)
    return f'Rating increased for {updated_movies_count} movies.'