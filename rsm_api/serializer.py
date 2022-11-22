from .models import RoadSignsForRepair, Area, RoadSign, Locality
from rest_framework import serializers


class RoadSignsForRepairSerializer(serializers.ModelSerializer):
    # mode = serializers.ChoiceField(RoadSignsForRepair.MODE_CATEGORIES, default="standard")

    class Meta:
        model = RoadSignsForRepair
        fields = [
            "id",
            "area",
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
        ]  # All fields


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = [
            "id",
            "name",
        ]  # All fields
