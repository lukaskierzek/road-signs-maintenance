from django.shortcuts import render
from django.views import generic
from .models import RoadSignsForRepair, Region
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class RoadSignsForRepairListView(LoginRequiredMixin, generic.ListView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair'
    template_name = 'road_signs_repair/index.html'


class RoadSignsForRepairDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair_detail'
    template_name = 'road_signs_repair/road_signs_for_repair_detail.html'
    permission_required = ('road_signs_repair.can_update_task',)


class RegionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Region
    context_object_name = 'region'
    template_name = 'road_signs_repair/region_detail.html'
