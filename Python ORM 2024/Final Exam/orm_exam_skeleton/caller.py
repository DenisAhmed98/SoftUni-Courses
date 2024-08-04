import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


from main_app.models import Astronaut,Mission,Spacecraft
from django.db.models import Q, Count, Sum, F, Avg


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    # Format the output string
    if astronauts.exists():
        return "\n".join(
            f"Astronaut: {a.name}, phone number: {a.phone_number}, status: {'Active' if a.is_active else 'Inactive'}"
            for a in astronauts
        )

    return ""


def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if top_astronaut is None or top_astronaut.mission_count == 0:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_count} missions."


def get_top_commander():
    top_commander = Astronaut.objects.annotate(
        num_commanded_missions=Count('mission_commander')
    ).order_by('-num_commanded_missions', 'phone_number').first()

    if not top_commander or top_commander.num_commanded_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_commanded_missions} commanded missions."


def get_last_completed_mission():
    last_mission = Mission.objects.filter(status="Completed").order_by('-launch_date').first()

    if not last_mission:
        return "No data."

    commander_name = last_mission.commander.name if last_mission.commander else "TBA"
    astronauts_names = ", ".join(
        last_mission.astronauts.order_by('name').values_list('name', flat=True)
    )
    total_spacewalks = last_mission.astronauts.aggregate(
        total_spacewalks=Sum('spacewalks')
    )['total_spacewalks'] or 0

    return (
        f"The last completed mission is: {last_mission.name}. "
        f"Commander: {commander_name}. Astronauts: {astronauts_names}. "
        f"Spacecraft: {last_mission.spacecraft.name}. Total spacewalks: {total_spacewalks}."
    )


def get_most_used_spacecraft():
    most_used_spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('mission_spacecraft')
    ).order_by('-num_missions', 'name').first()

    if not most_used_spacecraft or most_used_spacecraft.num_missions == 0:
        return "No data."

    num_astronauts = Astronaut.objects.filter(
        mission_astronauts__spacecraft=most_used_spacecraft
    ).distinct().count()

    return (
        f"The most used spacecraft is: {most_used_spacecraft.name}, "
        f"manufactured by {most_used_spacecraft.manufacturer}, "
        f"used in {most_used_spacecraft.num_missions} missions, "
        f"astronauts on missions: {num_astronauts}."
    )


def decrease_spacecrafts_weight():
    spacecrafts_to_update = Spacecraft.objects.filter(
        mission_spacecraft__status="Planned",
        weight__gte=200.0
    ).distinct()

    spacecrafts_affected = spacecrafts_to_update.update(weight=F('weight') - 200.0)

    if spacecrafts_affected == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (
        f"The weight of {spacecrafts_affected} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight:.1f}kg"
    )
