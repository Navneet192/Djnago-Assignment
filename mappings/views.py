from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from patients.models import Patient
from doctors.models import Doctor

class MappingCreateView(generics.CreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        patient_id = request.data.get("patient")
        doctor_id = request.data.get("doctor")

        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
        except Patient.DoesNotExist:
            return Response({"error": "Invalid patient ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response({"error": "Invalid doctor ID"}, status=status.HTTP_400_BAD_REQUEST)

        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            return Response({"message": "Mapping already exists"}, status=status.HTTP_409_CONFLICT)

        
        mapping = PatientDoctorMapping.objects.create(patient=patient, doctor=doctor)
        serializer = self.get_serializer(mapping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MappingListView(generics.ListAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]



class PatientDoctorListView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)



class MappingDeleteView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            mapping = self.get_object()
            mapping.delete()
            return Response({"message": "Mapping deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)