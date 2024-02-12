from django.db import models
from django.contrib.auth.models import User as UserProfile
from django.contrib import admin

class User(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    money = models.DecimalField(default=100, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.username
    

class BetHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.CharField(max_length=50)
    bet_amount = models.DecimalField(max_digits=10, decimal_places=2)
    win_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game} - {self.timestamp}"