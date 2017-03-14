from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "%s" % self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location)
    description = models.TextField()

    def __str__(self):
        return "%s" % self.year
