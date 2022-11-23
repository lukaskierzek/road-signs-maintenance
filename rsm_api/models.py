from django.db import models


# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of the area where there may be road signs",
                            verbose_name='Area name',
                            unique=True)

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of locality where there may be road sign",
                            verbose_name='Locality name',
                            unique=True)

    def __str__(self):
        return self.name


class RoadSign(models.Model):
    series = models.CharField(max_length=30,
                              help_text="Enter a series of the road sign",
                              unique=True)

    name = models.CharField(max_length=50,
                            help_text="Enter a name of road sign")

    description = models.TextField(max_length=500,
                                   help_text="Enter a description of the road signs")

    def __str__(self):
        return self.series


class RoadSignsForRepair(models.Model):
    area = models.ForeignKey(to=Area,
                             on_delete=models.SET_NULL,
                             related_name='areas',
                             null=True)

    locality = models.ForeignKey(to=Locality,
                                 on_delete=models.SET_NULL,
                                 related_name='localities',
                                 null=True)

    sign = models.ForeignKey(to=RoadSign,
                             on_delete=models.SET_NULL,
                             related_name='signs',
                             null=True)

    description_of_the_place = models.TextField(max_length=500,
                                                help_text="Enter a description of the place where road signs is to repair")

    task = models.CharField(max_length=255,
                            help_text="Enter a task to realize")

    report_date = models.DateField()

    repair_date = models.DateField()

    MODE_CATEGORIES = [
        (
            'standard', (
                ('S', 'STANDARD'),
            )
        ),
        (
            'priority', (
                ('P', 'PRIORITY'),
            )
        )
    ]
    mode = models.CharField(max_length=8,
                            choices=MODE_CATEGORIES,
                            default='standard',
                            help_text='Select a mode')

    def __str__(self):
        return f"{self.locality} | {self.area} | {self.sign} | {self.task}"
