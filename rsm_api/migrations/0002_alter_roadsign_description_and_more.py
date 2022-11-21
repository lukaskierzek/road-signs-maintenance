# Generated by Django 4.1.3 on 2022-11-20 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsm_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsign',
            name='description',
            field=models.TextField(help_text='Enter a description of the road signs', max_length=500),
        ),
        migrations.AlterField(
            model_name='roadsignsforrepair',
            name='description_of_the_place',
            field=models.TextField(help_text='Enter a description of the place where road signs is to repair', max_length=500),
        ),
    ]
