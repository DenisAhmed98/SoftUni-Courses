from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from django.db import models

from main_app.managers import AstronautManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )


class Astronaut(BaseModel):

    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex=r'^\d+$')])

    is_active = models.BooleanField(default=True)

    date_of_birth = models.DateField(null=True, blank=True)

    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    updated_at = models.DateTimeField(auto_now=True)

    objects = AstronautManager()


class Spacecraft(BaseModel):
    manufacturer = models.CharField(max_length=100)

    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    weight = models.FloatField(validators=[MinValueValidator(0.0)])

    launch_date = models.DateField()

    updated_at = models.DateTimeField(auto_now=True)


class MissionChoices(models.TextChoices):
    Planned = "Planned", "Planned"
    Ongoing = "Ongoing", "Ongoing"
    Completed = "Completed", "Completed"


class Mission(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        choices=MissionChoices.choices,
        max_length=9,
        default=MissionChoices.Planned
    )

    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    spacecraft = models.ForeignKey(to=Spacecraft, on_delete=models.CASCADE, related_name='mission_spacecraft')
    astronauts = models.ManyToManyField(to=Astronaut,  related_name='mission_astronauts')
    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        related_name='mission_commander',
        null=True
    )
