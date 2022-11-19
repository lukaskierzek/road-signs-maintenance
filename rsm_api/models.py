from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of the region where there may be road signs",
                            verbose_name='Region name')

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of locality where there may be road sign",
                            verbose_name='Locality name')

    region = models.ForeignKey(to=Region,
                               on_delete=models.SET_NULL,
                               null=True)

    def __str__(self):
        return self.name


class RoadSign(models.Model):
    series = models.CharField(max_length=30,
                              help_text="Enter a series of the road sign")

    name = models.CharField(max_length=50,
                            help_text="Enter a name of road sign")

    description = models.CharField(max_length=500,
                                   help_text="Enter a description of the road signs")


class RoadSignsForRepair(models.Model):
    region = models.ForeignKey(to=Region,
                               on_delete=models.SET_NULL,
                               null=True)

    locality = models.ForeignKey(to=Locality,
                                 on_delete=models.SET_NULL,
                                 null=True)

    sign = models.ForeignKey(to=RoadSign,
                             on_delete=models.SET_NULL,
                             null=True)

    description_of_the_place = models.CharField(max_length=500,
                                                help_text="Enter a description of the place where road signs is to repair")

    task = models.CharField(max_length=255,
                            help_text="Enter a task to realize")

    report_date = models.DateField()

    repair_date = models.DateField()
