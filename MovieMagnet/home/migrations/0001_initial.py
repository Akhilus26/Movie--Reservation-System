# Generated by Django 5.0 on 2024-01-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='picture')),
                ('trailer', models.URLField(default=None)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cast', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('hindi', 'Hindi'), ('malayalam', 'Malayalam'), ('tamil', 'Tamil'), ('english', 'English')], max_length=255)),
                ('release_date', models.DateField()),
                ('runtime', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('in', 'In'), ('out', 'Out'), ('soon', 'Soon')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=50)),
                ('role', models.CharField(choices=[('customer', 'customer'), ('admin', 'admin')], default='customer', max_length=100)),
            ],
        ),
    ]
