from django.contrib import admin
from .models import Locality, RoadSign, RoadSignsForRepair, Region


# Register your models here.
# Login: Admin
# Password: zaq1@WSX


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    pass


@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    pass


@admin.register(RoadSignsForRepair)
class RoadSignsForRepairAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass
