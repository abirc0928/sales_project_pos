# Generated by Django 5.1.1 on 2024-10-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
