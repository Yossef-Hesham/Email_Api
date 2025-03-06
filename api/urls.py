from django.urls import path
from .views import EmaiMessageCreateAPIView

urlpatterns = [
    path('', EmaiMessageCreateAPIView.as_view()),
]
