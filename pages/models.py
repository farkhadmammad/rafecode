from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    konu = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField (max_length=30)
    message = models.TextField(blank=True)



    def __str__(self):
        return self.email
    

