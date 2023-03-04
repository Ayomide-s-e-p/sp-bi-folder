from django.db import models

# Create your models here.
class client_info(models.Model):
    email = models.EmailField(max_length=250)
    phone = models.Inter()
    pwd = models.TextField(max_length=500)
    Confirmpwd = models.TextField(max_length=500)
    message = models.TextField(max_length=15000)
    
    def __str__(self) -> str:
        return self.email