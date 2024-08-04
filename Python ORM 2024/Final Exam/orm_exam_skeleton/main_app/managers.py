from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self.annotate(mission_count=Count('mission_astronauts')).order_by('-mission_count', 'phone_number')
