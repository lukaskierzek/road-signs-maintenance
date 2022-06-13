# Generated by Django 4.0.5 on 2022-06-13 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of locality where there may be road sign', max_length=100, verbose_name='localities')),
            ],
            options={
                'verbose_name_plural': 'localities',
                'ordering': ['name'],
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the region where there may be road signs', max_length=100, verbose_name='names')),
            ],
            options={
                'verbose_name_plural': 'names',
                'ordering': ['name'],
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='RoadSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(help_text='Enter a series of the road sign', max_length=30)),
                ('name', models.CharField(help_text='Enter a name of road sign', max_length=50)),
                ('description', models.TextField(help_text='Enter a description of the road signs', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RoadSignsForRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_of_the_place', models.TextField(help_text='Enter a description of the place where road signs is to repair', max_length=500)),
                ('task', models.CharField(help_text='Enter a task to realize', max_length=255)),
                ('report_date', models.DateField()),
                ('repair_date', models.DateField()),
                ('mode', models.CharField(choices=[('standard', (('S', 'STANDARD'),)), ('priority', (('P', 'PRIORITY'),))], default='standard', help_text='Select a mode', max_length=8, null=True)),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='road_signs_repair.locality')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='road_signs_repair.region')),
                ('sign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='road_signs_repair.roadsign')),
            ],
            options={
                'ordering': ['region', 'locality'],
                'permissions': (),
            },
        ),
        migrations.AddField(
            model_name='locality',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='road_signs_repair.region'),
        ),
    ]
