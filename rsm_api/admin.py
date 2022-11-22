from django.contrib import admin
from .models import Locality, RoadSign, RoadSignsForRepair, Area


# Register your models here.
# Login: admin
# Password: admin

class LocalityInline(admin.TabularInline):
    model = Locality
    extra = 0
    fields = [
        "name",
        "area",
    ]


class RoadSignsForRepairInline(admin.TabularInline):
    model = RoadSignsForRepair
    extra = 0
    fields = [
        "area",
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
    list_display = ("__str__",)

    search_fields = [
        "name",
    ]

    fieldsets = [
        (None, {'fields': ['name']}),
    ]

    inlines = [RoadSignsForRepairInline]


@admin.register(RoadSign)
class RoadSignAdmin(admin.ModelAdmin):
    list_display = ("__str__",
                    "name",
                    "description",)

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
                    "area",
                    "locality",
                    "sign",
                    "description_of_the_place",
                    "task",
                    "mode",
                    "report_date",
                    "repair_date",)

    list_filter = ("area",
                   "locality",
                   "sign",
                   "task",
                   "mode",
                   "report_date",
                   "repair_date",)

    search_fields = [
        "description_of_the_place",
        "area",
        "sign",
        "mode",
    ]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

    list_filter = ("name",)

    search_fields = ["name", ]

    inlines = [RoadSignsForRepairInline]
