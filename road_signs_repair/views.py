from django.shortcuts import render
from django.views import generic
from .models import RoadSignsForRepair, Region


# Create your views here.
class RoadSignsForRepairListView(generic.ListView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair'
    template_name = 'road_signs_repair/index.html'


class RoadSignsForRepairDetailView(generic.DetailView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair_detail'
    template_name = 'road_signs_repair/road_signs_for_repair_detail.html'


class RegionDetailView(generic.DetailView):
    model = Region
    context_object_name = 'region'
    template_name = 'road_signs_repair/region_detail.html'
