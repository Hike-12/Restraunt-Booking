# Generated by Django 5.1 on 2024-10-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event_eventschedule_tablebooking_delete_events_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablebooking',
            name='event_schedule',
        ),
        migrations.RemoveField(
            model_name='tablebooking',
            name='user',
        ),
        migrations.AlterField(
            model_name='chef',
            name='availability',
            field=models.CharField(max_length=50),
        ),
    ]
