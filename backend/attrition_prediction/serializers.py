from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeDataSerializer(serializers.ModelSerializer):
    # Nested Employee serializer to show details
    class Meta:
        model = Employee_Data
        fields = '__all__'  # Includes all fields in the Employee_Data model

class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = '__all__'

class ChatMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
