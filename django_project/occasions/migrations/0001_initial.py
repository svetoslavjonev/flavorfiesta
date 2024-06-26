# Generated by Django 5.0.2 on 2024-03-27 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chefs', '0003_alter_chef_image'),
        ('events', '0006_eventcomment'),
        ('venues', '0003_alter_venue_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occasions', to='chefs.chef')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occasions', to='events.event')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occasions', to='venues.venue')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
    ]
