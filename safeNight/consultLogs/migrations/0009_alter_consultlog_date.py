# Generated by Django 4.2.13 on 2024-06-27 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultLogs', '0008_alter_consultlog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultlog',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 27, 13, 21, 51, 106538, tzinfo=datetime.timezone.utc), verbose_name='작성일'),
        ),
    ]
