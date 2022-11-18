from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView
from .models import RoadSignsForRepair, Region
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class RoadSignsForRepairListView(LoginRequiredMixin, ListView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair'
    template_name = 'road_signs_repair/index.html'


class RoadSignsForRepairDetailView(LoginRequiredMixin, DetailView):
    model = RoadSignsForRepair
    context_object_name = 'road_signs_for_repair_detail'
    template_name = 'road_signs_repair/road_signs_for_repair_detail.html'


class RoadSignsForRepairUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RoadSignsForRepair
    fields = [
        'region',
        'locality',
        'sign',
        'description_of_the_place',
        'task',
        'mode',
        'report_date',
        'repair_date',
    ]
    template_name = 'road_signs_repair/road_signs_for_repair_form.html'
    permission_required = ('road_signs_repair.can_update_task',)
    context_object_name = 'road_signs_for_repair_update'


class RegionDetailView(LoginRequiredMixin, DetailView):
    model = Region
    context_object_name = 'region'
    template_name = 'road_signs_repair/region_detail.html'
