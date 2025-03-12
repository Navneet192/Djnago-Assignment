from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'experience', 'phone']  

    def create(self, validated_data):
        request = self.context.get('request')
        doctor = Doctor.objects.create(**validated_data)
        return doctor