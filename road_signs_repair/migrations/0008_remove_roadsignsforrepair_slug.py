# Generated by Django 4.0.5 on 2022-08-18 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('road_signs_repair', '0007_locality_slug_roadsign_slug_roadsignsforrepair_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadsignsforrepair',
            name='slug',
        ),
    ]
