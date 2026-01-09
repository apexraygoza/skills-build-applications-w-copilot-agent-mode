
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from django.utils import timezone
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Use raw MongoDB deletion to avoid Djongo ORM issues
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.user.delete_many({})
        db.workout.delete_many({})
        db.team.delete_many({})

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_leader=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_leader=True),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Cardio Blast', description='High intensity cardio', difficulty='Hard'),
            Workout(name='Strength Training', description='Build muscle', difficulty='Medium'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        Activity.objects.create(user=users[0], workout=workouts[0], date=timezone.now(), duration_minutes=30, calories_burned=300)
        Activity.objects.create(user=users[1], workout=workouts[1], date=timezone.now(), duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workouts[0], date=timezone.now(), duration_minutes=25, calories_burned=250)
        Activity.objects.create(user=users[3], workout=workouts[1], date=timezone.now(), duration_minutes=50, calories_burned=420)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, total_points=700, rank=1)
        Leaderboard.objects.create(team=dc, total_points=670, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
