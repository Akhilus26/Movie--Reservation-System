# Generated by Django 5.0 on 2024-01-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('movie_name', models.CharField(max_length=255)),
                ('theater_name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('seatnumber', models.CharField(max_length=255)),
                ('totalseats', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
