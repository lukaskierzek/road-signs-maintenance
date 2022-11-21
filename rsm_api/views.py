from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .serializer import RoadSignsForRepairSerializer, RoadSignSerializer, LocalitySerializer, RegionSerializer
from .models import RoadSignsForRepair, Region, RoadSign, Locality


class RoadSignsForRepairList(generics.ListCreateAPIView):
    serializer_class = RoadSignsForRepairSerializer
    queryset = RoadSignsForRepair.objects.all()


class RoadSignsForRepairDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoadSignsForRepairSerializer
    queryset = RoadSignsForRepair.objects.all()


class RoadSignList(generics.ListCreateAPIView):
    serializer_class = RoadSignSerializer
    queryset = RoadSign.objects.all()


class RoadSignDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoadSignSerializer
    queryset = RoadSign.objects.all()


class LocalityList(generics.ListCreateAPIView):
    serializer_class = LocalitySerializer
    queryset = Locality.objects.all()


class LocalityDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocalitySerializer
    queryset = Locality.objects.all()


class RegionList(generics.ListCreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
