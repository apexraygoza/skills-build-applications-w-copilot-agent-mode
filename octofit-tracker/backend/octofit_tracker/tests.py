from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='A test workout', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        workout = Workout.objects.create(name='Test Workout', description='A test workout', difficulty='Easy')
        activity = Activity.objects.create(user=user, workout=workout, date='2026-01-08T00:00:00Z', duration_minutes=30, calories_burned=200)
        self.assertEqual(activity.duration_minutes, 30)

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)
