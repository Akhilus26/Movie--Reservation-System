# Generated by Django 5.0 on 2024-02-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_seats_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='time',
            field=models.CharField(choices=[('05:00 AM', '5:00 AM'), ('10:10 AM', '10:10 AM'), ('02:15 PM', '2:15 PM'), ('05:30 PM', '5:30 PM'), ('08:30 PM', '8:30 PM'), ('11:45 PM', '11:45 PM')], max_length=255),
        ),
    ]
