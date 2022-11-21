from .models import RoadSignsForRepair, Region, RoadSign, Locality
from rest_framework import serializers


class RoadSignsForRepairSerializer(serializers.ModelSerializer):
    # mode = serializers.ChoiceField(RoadSignsForRepair.MODE_CATEGORIES, default="standard")

    class Meta:
        model = RoadSignsForRepair
        fields = [
            "id",
            "region",
            "locality",
            "sign",
            "description_of_the_place",
            "task",
            "mode",
            "report_date",
            "repair_date",
        ]  # All fields


class RoadSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSign
        fields = [
            "id",
            "series",
            "name",
            "description",
        ]  # All fields


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = [
            "id",
            "name",
            "region",
        ]  # All fields


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            "id",
            "name",
        ]  # All fields
