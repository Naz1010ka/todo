from django.db import models

class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.IntegerField(default= True)
    date_of_meeting = models.DateTimeField(auto_now_add = True)
    comment = models.TextField(default="")
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Goal_for_month(models.Model):
    Goal = models.CharField(max_length=100)
    Month = models.DateTimeField(auto_now_add=True)
    difficulty = models.FloatField(default="")
    reason_for_goal = models.TextField(default="")
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)