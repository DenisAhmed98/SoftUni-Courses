import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Article,Author,Review

# Create queries within functions


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    if search_name is not None and search_email is not None:
        query = Author.objects.filter(
            full_name__icontains=search_name,
            email__icontains=search_email
        ).order_by('-full_name')
    elif search_name is not None:
        query = Author.objects.filter(
            full_name__icontains=search_name
        ).order_by('-full_name')
    else:
        query = Author.objects.filter(
            email__icontains=search_email
        ).order_by('-full_name')

    if query.exists():
        return "\n".join(
            f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}"
            for a in query
        )
    return ""


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if top_author is None or top_author.article_count == 0:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.article_count} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(
        reviews_count=Count('review')
    ).order_by('-reviews_count', 'email').first()

    if top_reviewer is None or top_reviewer.reviews_count == 0:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.reviews_count} published reviews."





def get_latest_article():
    # Retrieve the latest article based on the 'published_on' date
    latest_article = Article.objects.order_by('-published_on').first()

    # Check if there are no articles
    if not latest_article:
        return ""

    # Get authors of the latest article, ordered by full name
    authors = latest_article.authors.order_by('full_name').all()
    author_names = ", ".join(author.full_name for author in authors)

    # Calculate the number of reviews and average rating for the article
    num_reviews = latest_article.review_set.count()
    avg_rating = latest_article.review_set.aggregate(average_rating=Avg('rating'))['average_rating'] or 0

    # Format average rating to two decimal places
    avg_rating_formatted = f"{avg_rating:.2f}"

    # Format the result string
    return (
        f"The latest article is: {latest_article.title}. "
        f"Authors: {author_names}. "
        f"Reviewed: {num_reviews} times. "
        f"Average Rating: {avg_rating_formatted}."
    )

def get_top_rated_article():
    # Annotate articles with the average rating and number of reviews
    articles_with_ratings = Article.objects.annotate(
        avg_rating=Avg('review__rating'),
        num_reviews=Count('review')
    )

    # Filter to get articles with at least one review
    articles_with_reviews = articles_with_ratings.filter(num_reviews__gt=0)

    # Check if there are no articles with reviews
    if not articles_with_reviews.exists():
        return ""

    # Order articles by average rating (descending) and title (ascending)
    top_article = articles_with_reviews.order_by('-avg_rating', 'title').first()

    # Format the average rating to two decimal places
    avg_rating_formatted = f"{top_article.avg_rating:.2f}"

    # Format the result string
    return (
        f"The top-rated article is: {top_article.title}, "
        f"with an average rating of {avg_rating_formatted}, "
        f"reviewed {top_article.num_reviews} times."
    )


def ban_author(email=None):
    # Check if the email is provided and not None
    if email is None:
        return "No authors banned."

    try:
        # Retrieve the author by email
        author = Author.objects.get(email=email)
    except Author.DoesNotExist:
        # Return if the author does not exist
        return "No authors banned."

    # Count the number of reviews by the author
    num_reviews = Review.objects.filter(author=author).count()

    # Delete all reviews by the author
    Review.objects.filter(author=author).delete()

    # Change the author's status to banned
    author.is_banned = True
    author.save()

    # Return the result string
    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."