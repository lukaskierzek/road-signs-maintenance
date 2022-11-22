from django.urls import path
from .views import (
    RoadSignsForRepairList,
    RoadSignsForRepairDetail,
    RoadSignList,
    RoadSignDetail,
    LocalityList,
    LocalityDetail,
    AreaList,
    AreaDetail
)

app_name = 'rsm_api'

urlpatterns = [
    path('road-signs-for-repair/', RoadSignsForRepairList.as_view(), name='road_signs_for_repair_list'),
    path('road-signs-for-repair/<int:pk>', RoadSignsForRepairDetail.as_view(), name='road_signs_for_repair_detail'),
    path('road-signs/', RoadSignList.as_view(), name='road_sign_list'),
    path('road-signs/<int:pk>', RoadSignDetail.as_view(), name='road_sign_detail'),
    path('locality/', LocalityList.as_view(), name='locality_list'),
    path('locality/<int:pk>', LocalityDetail.as_view(), name='locality_detail'),
    path('area/', AreaList.as_view(), name='area_list'),
    path('area/<int:pk>', AreaDetail.as_view(), name='area_detail'),
]
