from django.db import models
from django.http import request

# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True, null=True, blank=True)# the date on which the appointment message was sent
    accepted = models.BooleanField(default=False) # to capture the state of the appointment whether it has been accepted or not
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True) #date on which the appointment will take place. The date will be set manually

    def __str__(self): # display the first name as a reference for the object name
        return self.first_name
    
    class Meta: # order the appointments by the date when the appointment was made
        ordering = ["-sent_date"]