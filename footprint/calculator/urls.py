from django.urls import path
from . import views
from .views import OfficeOperationFormUpdateView, OfficeOperationFormDeleteView

urlpatterns = [
    path("", views.office_operation_form_view, name="calculator"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("view_data/", views.view_data, name="view_data"),
    path('update/<int:pk>/', OfficeOperationFormUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OfficeOperationFormDeleteView.as_view(), name='delete'),
]