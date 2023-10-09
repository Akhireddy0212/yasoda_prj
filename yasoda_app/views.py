from django.shortcuts import render
from django.views import View

from .models import Patient, Doctor, Appointment

class AppointmentListView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'appointment_list.html', {'appointments': appointments})

class PatientListView(View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'patient_list.html', {'patients': patients})

class DoctorListView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'doctor_list.html', {'doctors': doctors})


# Create your views here.
