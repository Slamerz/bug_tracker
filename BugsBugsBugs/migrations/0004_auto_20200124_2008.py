# Generated by Django 3.0.2 on 2020-01-24 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BugsBugsBugs', '0003_auto_20200124_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_Filed',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 20, 8, 9, 921086, tzinfo=utc), verbose_name='dateFiled'),
        ),
    ]
