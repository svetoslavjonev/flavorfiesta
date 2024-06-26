# Generated by Django 5.0.2 on 2024-03-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='Limit of 1500 characters', max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
