from django.contrib import admin
from .models import Locality, RoadSign, RoadSignsForRepair, Region


# Register your models here.
# Login: Admin
# Password: zaq1@WSX

class LocalityInline(admin.TabularInline):
    model = Locality
    extra = 0
    fields = [
        "name",
        "region",
    ]


class RoadSignsForRepairInline(admin.TabularInline):
    model = RoadSignsForRepair
    extra = 0
    fields = [
        "region",
        "locality",
        "sign",
        "description_of_the_place",
        "task",
        "mode",
        "report_date",
        "repair_date",
    ]


@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ("__str__",
                    "region",
                    "slug",)

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_filter = ("region",)

    search_fields = [
        "name",
        "region__name",
    ]

    fieldsets = [
        (None, {'fields': ['name', 'slug']}),
        ('Region', {'fields': ['region']}),
    ]

    inlines = [RoadSignsForRepairInline]


@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ("__str__",
                    "name",
                    "description",
                    "slug",)

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_filter = ("series",)

    search_fields = [
        "series",
        "name",
        "description",
    ]

    inlines = [RoadSignsForRepairInline]


@admin.register(RoadSignsForRepair)
class RoadSignsForRepairAdmin(admin.ModelAdmin):
    list_display = ("__str__",
                    "region",
                    "locality",
                    "sign",
                    "description_of_the_place",
                    "task",
                    "mode",
                    "report_date",
                    "repair_date",)

    list_filter = ("region",
                   "locality",
                   "sign",
                   "task",
                   "mode",
                   "report_date",
                   "repair_date",)

    search_fields = [
        "description_of_the_place",
        "region",
        "sign",
        "mode",
    ]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("__str__",
                    "slug",)

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_filter = ("name",)

    search_fields = ["name", ]

    inlines = [LocalityInline, RoadSignsForRepairInline]
