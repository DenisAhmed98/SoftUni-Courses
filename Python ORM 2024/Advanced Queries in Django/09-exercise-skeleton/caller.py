import os
from datetime import date

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import RealEstateListing, Invoice, BillingInfo, Task, Exercise

# Run and print your queries
# Create instances of Exercise
