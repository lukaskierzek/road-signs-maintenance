# Generated by Django 4.1.3 on 2022-11-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsm_api', '0002_alter_roadsign_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadsignsforrepair',
            name='mode',
            field=models.CharField(choices=[('standard', (('S', 'STANDARD'),)), ('priority', (('P', 'PRIORITY'),))], default='standard', help_text='Select a mode', max_length=8),
        ),
    ]