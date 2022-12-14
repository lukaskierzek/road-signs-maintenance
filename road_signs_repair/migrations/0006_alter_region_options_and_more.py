# Generated by Django 4.0.5 on 2022-08-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('road_signs_repair', '0005_alter_locality_table_alter_region_table_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['name'], 'permissions': (), 'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='roadsignsforrepair',
            options={'ordering': ['report_date', 'repair_date'], 'permissions': (), 'verbose_name_plural': 'road signs for repair'},
        ),
        migrations.AddField(
            model_name='region',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='locality',
            name='name',
            field=models.CharField(help_text='Enter the name of locality where there may be road sign', max_length=100, verbose_name='Locality name'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(help_text='Enter the name of the region where there may be road signs', max_length=100, verbose_name='Region name'),
        ),
    ]
