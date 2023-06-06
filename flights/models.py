from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # models.CASCADE means, if we delete an airport from the airports table, its going to delete any of the corresponding flights
    # related_name allows you access a relationship in the opposite direction
    # in this case it would give us all the flights that have that airport as the origin
    # when we modify a model, it doesn't automatically reflect in the db. it's a two step process
    # First, we run python3 manage.py makemigrations, so it looks for changes and automatically makes a migration instruction file
    # Second, we run python3 manage.py migrate, to apply the migrations
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"