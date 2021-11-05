from django.db import models


class Data(models.Model):
    previos = models.IntegerField()
    now = models.IntegerField()
