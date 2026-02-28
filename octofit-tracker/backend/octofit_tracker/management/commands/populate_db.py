from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='marvel', description='Marvel Team')
            dc = Team.objects.create(name='dc', description='DC Team')

            self.stdout.write(self.style.SUCCESS('Creating users...'))

            users = [
                User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name),
                User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name),
                User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name),
                User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name),
            ]

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user_email='tony@stark.com', type='run', duration=30, date='2024-01-01')
            Activity.objects.create(user_email='steve@rogers.com', type='cycle', duration=45, date='2024-01-02')
            Activity.objects.create(user_email='bruce@wayne.com', type='swim', duration=25, date='2024-01-03')
            Activity.objects.create(user_email='clark@kent.com', type='yoga', duration=60, date='2024-01-04')

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(team_name=marvel.name, points=150)
            Leaderboard.objects.create(team_name=dc.name, points=120)

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
            Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
            Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='hard')

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
