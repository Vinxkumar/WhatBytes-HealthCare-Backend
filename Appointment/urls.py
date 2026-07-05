from django.urls import path

from .views import (
    MappingListCreateView,
    PatientMappingView,
    MappingDeleteView
)


urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create"
    ),

    path(
        "<int:id>/",
        PatientMappingView.as_view(),
        name="mapping-detail"
    ),
    path(
        "doc/<int:id>/",
        MappingDeleteView.as_view(),
        name="delete-mapping-detail"
    ),
]