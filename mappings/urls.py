from django.urls import path
from .views import MappingCreateView, MappingListView, PatientDoctorListView, MappingDeleteView

urlpatterns = [
    path('', MappingListView.as_view(), name='list-mappings'),
    path('assign/', MappingCreateView.as_view(), name='assign-doctor'),
    path('<int:patient_id>/', PatientDoctorListView.as_view(), name='patient-doctor-list'),
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='remove-mapping'),
]