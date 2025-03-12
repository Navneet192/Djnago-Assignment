from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id' , 'name', 'age', 'gender', 'address', 'phone']

    def create(self, validated_data):
        request = self.context.get("request")  
        if request and hasattr(request, "user"):
            validated_data["user"] = request.user  
        return super().create(validated_data)