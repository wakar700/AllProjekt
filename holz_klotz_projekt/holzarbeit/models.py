from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Holzarten(models.Model):
    holzart = models.CharField(max_length=100)
    festmeter = models.FloatField()
    betrag = models.FloatField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.holzart


class Brett(models.Model):
    brettnummer = models.CharField(max_length=100)
    holzart = models.CharField(max_length=100)
    laenge = models.FloatField()
    breite = models.FloatField()
    staerke = models.FloatField()

    def __str__(self):
        return self.brettnummer

    def get_absolute_url(self):
        return reverse('brett-create')


class Scheiben(models.Model):
    scheibennummer = models.CharField(max_length=100)
    holzart = models.CharField(max_length=100)
    durchmesser = models.FloatField()
    staerke = models.FloatField()

    def __str__(self):
        return self.scheibennummer


class Holz(models.Model):
    name = models.CharField(max_length=100)
    preis = models.FloatField()

    def __str__(self):
        return self.name