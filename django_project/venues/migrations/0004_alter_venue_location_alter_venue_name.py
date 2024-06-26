# Generated by Django 5.0.2 on 2024-04-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0003_alter_venue_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='location',
            field=models.CharField(default='Unknown', help_text='Enter city and country separated by a comma.', max_length=60),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
