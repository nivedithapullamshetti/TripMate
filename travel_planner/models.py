from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()

    transport = models.CharField(max_length=50)
    accommodation = models.CharField(max_length=100)
    activities = models.CharField(max_length=200)

    def __str__(self):
        return self.destination