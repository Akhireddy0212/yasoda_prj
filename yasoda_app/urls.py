from django.urls import path
from .views import AppointmentListView, PatientListView, DoctorListView

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
]
