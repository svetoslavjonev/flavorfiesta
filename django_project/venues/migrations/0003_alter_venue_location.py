# Generated by Django 5.0.2 on 2024-03-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_venue_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='location',
            field=models.CharField(default='Unknown', help_text='Enter city and country separated by a comma.', max_length=50),
        ),
    ]
