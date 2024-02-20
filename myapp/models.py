from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank = False)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)


    def __str__(self):
        return f"{self.first_name}{self.last_name}"



