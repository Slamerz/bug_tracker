from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    NEW = 'NEW'
    IN_PROGRESS = 'INPROGRESS'
    DONE = 'DONE'
    INVALID = 'INVALID'
    CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    title = models.CharField(max_length=180)
    date_Filed = models.DateTimeField('dateFiled', default=timezone.now())
    description = models.CharField(max_length=300)
    filed_By = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='filed_By',
        blank=True,
        null=True,)
    assigned_To = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_To',
        blank=True,
        null=True,)
    completed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='completed_by',
        blank=True,
        null=True)
    status = models.CharField(choices=CHOICES, max_length=11, default=NEW)

    def __str__(self):
        return f'{self.title}'
