# Generated by Django 4.0.5 on 2022-06-19 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('road_signs_repair', '0002_alter_roadsign_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='road_signs_repair.region'),
        ),
        migrations.AlterField(
            model_name='roadsignsforrepair',
            name='locality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='road_signs_repair.locality'),
        ),
        migrations.AlterField(
            model_name='roadsignsforrepair',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='road_signs_repair.region'),
        ),
        migrations.AlterField(
            model_name='roadsignsforrepair',
            name='sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='road_signs_repair.roadsign'),
        ),
    ]
