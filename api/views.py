from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from .serializers import EmailFormSerializer
import os

class EmaiMessageCreateAPIView(generics.CreateAPIView):
    serializer_class = EmailFormSerializer

    def perform_create(self, serializer):
        contact_message = serializer.save()
        send_mail(
        subject=contact_message.subject,
        message=f"From: {contact_message.name}\n\nMy email: {contact_message.email}\n\nMessage:\n{contact_message.text}",
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[os.getenv('reciever_email')],  
        fail_silently=False
)

