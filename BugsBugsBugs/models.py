from django.db import models

class Ticket(models.Model):
    title = models.CharField()
