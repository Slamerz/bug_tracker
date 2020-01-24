from django.db import models


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
    date_Filed = models.DateTimeField('dateFiled', auto_now=True)
    description = models.CharField(max_length=300)
    filed_By = models.CharField(max_length=50)
    assigned_To = models.CharField(max_length=50)
    completed_by = models.CharField(max_length=50)
    status = models.CharField(choices=CHOICES, max_length=11, default=NEW)

    def __str__(self):
        return f'{self.title}'
