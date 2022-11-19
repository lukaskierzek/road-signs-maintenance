from django.urls import path, include

from . import views

app_name = 'road_signs_repair'

urlpatterns = [
    path('', views.RoadSignsForRepairListView.as_view(), name='road_signs_for_repair'),
    path('region/<slug:slug>', views.RegionDetailView.as_view(), name='region'),
    path('task/', include([
        path('<int:pk>', views.RoadSignsForRepairDetailView.as_view(), name='road_signs_for_repair_detail'),
        path('<int:pk>/update', views.RoadSignsForRepairUpdate.as_view(), name='road_signs_for_repair_update'),
    ])),
]
