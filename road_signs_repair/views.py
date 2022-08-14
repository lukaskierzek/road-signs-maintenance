from django.shortcuts import render
from django.views import generic
from .models import RoadSignsForRepair, Region


# Create your views here.
class RoadSignsForRepairListView(generic.ListView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair'
    template_name = 'road_signs_repair/index.html'


class RegionDetailView(generic.DetailView):
    model = Region
    context_object_name = 'region'
    template_name = 'road_signs_repair/region_detail.html'