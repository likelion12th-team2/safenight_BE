# Generated by Django 4.2.13 on 2024-06-27 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consultLogs', '0010_alter_consultlog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultlog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일'),
        ),
    ]
