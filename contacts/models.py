from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_request = models.CharField(max_length=250)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField()
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.car_title},{self.email}'
