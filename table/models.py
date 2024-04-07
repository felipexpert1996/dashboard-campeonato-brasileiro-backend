from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, null=False)

class Stadium(models.Model):
    name = models.CharField(max_length=100, null=False)

class Formation(models.Model):
    formation = models.CharField(max_length=50, null=False)

class Coach(models.Model):
    name = models.CharField(max_length=100, null=False)

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    visiting_team  = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_team')
    home_scoreboard = models.IntegerField()
    visiting_scoreboard = models.IntegerField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    home_formation = models.ForeignKey(Formation, on_delete=models.CASCADE, null=True, related_name='home_formation')
    visiting_formation = models.ForeignKey(Formation, on_delete=models.CASCADE, null=True, related_name='visiting_formation')
    home_coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, related_name='home_coach')
    visiting_coach = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, related_name='visiting_coach')
    game = models.IntegerField()