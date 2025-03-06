from rest_framework import serializers
from .models import EmailForm

class EmailFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailForm
        fields = ['name', 'email','subject', 'text', 'created_at']
