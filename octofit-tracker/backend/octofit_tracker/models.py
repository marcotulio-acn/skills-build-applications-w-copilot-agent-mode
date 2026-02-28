from djongo import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)  # nombre del equipo
    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()  # referencia manual al usuario
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"


class Leaderboard(models.Model):
    team_name = models.CharField(max_length=50)  # referencia manual al equipo
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team_name} - {self.points}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    def __str__(self):
        return self.name
