from rest_framework import generics
from django.core.mail import send_mail
from .serializers import EmailFormSerializer

class EmaiMessageCreateAPIView(generics.CreateAPIView):
    serializer_class = EmailFormSerializer

    def perform_create(self, serializer):
        contact_message = serializer.save()
        send_mail(
        subject=contact_message.subject,
        message=f"From: {contact_message.name}\n\n Message:\n{contact_message.text}",
        from_email=contact_message.email,
        recipient_list=["youssifhamdy381@gmail.com"],  
        fail_silently=False
)

