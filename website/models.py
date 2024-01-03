from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    address = models.CharField(max_length=150)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")