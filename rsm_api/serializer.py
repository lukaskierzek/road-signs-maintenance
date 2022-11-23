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
    signs = serializers.StringRelatedField(many=True)

    class Meta:
        model = RoadSign
        fields = [
            "id",
            "series",
            "name",
            "description",
            "signs",
        ]  # All fields


class LocalitySerializer(serializers.ModelSerializer):
    localities = serializers.StringRelatedField(many=True)

    class Meta:
        model = Locality
        fields = [
            "id",
            "name",
            "localities",
        ]  # All fields


class AreaSerializer(serializers.ModelSerializer):
    areas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Area
        fields = [
            "id",
            "name",
            "areas",
        ]  # All fields
