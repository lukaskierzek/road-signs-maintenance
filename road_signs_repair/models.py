from django.db import models
from django.urls import reverse


# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of the region where there may be road signs",
                            verbose_name='Region name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('road_signs_repair:region', kwargs={
            'pk': self.id,
        })

    class Meta:
        permissions = ()
        ordering = ['name']
        verbose_name_plural = 'Regions'
        db_table = 'region'


class Locality(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter the name of locality where there may be road sign",
                            verbose_name='Locality name')
    region = models.ForeignKey(to=Region,
                               on_delete=models.SET_NULL,
                               null=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = ()
        ordering = ['name']
        verbose_name_plural = 'localities'
        db_table = 'locality'


class RoadSign(models.Model):
    series = models.CharField(max_length=30,
                              help_text="Enter a series of the road sign")
    name = models.CharField(max_length=50,
                            help_text="Enter a name of road sign")
    description = models.TextField(max_length=500,
                                   help_text="Enter a description of the road signs")

    def __str__(self):
        return f"{self.series}"

    class Meta:
        permissions = ()
        ordering = ['series']
        verbose_name_plural = 'Road signs'
        db_table = 'road_sign'


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
                            null=True,
                            choices=MODE_CATEGORIES,
                            default='standard',
                            help_text='Select a mode')

    def __str__(self):
        return f"{self.region} - {self.locality} - {self.sign} - {self.task}"

    class Meta:
        permissions = ()
        ordering = ['region', 'locality']
        verbose_name_plural = 'road signs for repair'
        db_table = 'road_signs_for_repair'

# TODO: Add permissions to Meta in all Classes
