from django.db import models

# Create your models here.


class EmailForm(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.TextField(max_length=50, null=False, blank=True, default="No subject")
    text = models.TextField(max_length=10000,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    

    
    