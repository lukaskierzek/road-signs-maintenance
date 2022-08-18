from django.urls import path

from . import views

app_name = 'road_signs_repair'

urlpatterns = [
    path('', views.RoadSignsForRepairListView.as_view(), name='road_signs_for_repair'),
    path('region/<slug:slug>', views.RegionDetailView.as_view(), name='region')
]
