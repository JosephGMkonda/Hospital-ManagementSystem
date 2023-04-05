from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
import datetime



class CustomUser(AbstractUser):
    ADMINISTRATOR = '1'
    DOCTOR = '2'
    NURSE = '3'

    EMAIL_TYPE = {
        'admin' : ADMINISTRATOR,
        'doctor' : DOCTOR,
        'nurse' : NURSE
    }

    user_type = (
        (ADMINISTRATOR,"ADMINISTRATOR"),
        (DOCTOR,"DOCTOR"),
        (NURSE,"NURSE")
    )

    user = models.CharField(max_length=20, choices=user_type, default=1)

class Administrator(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=255)
    Gender = models.CharField(max_length=50)
    Contact_Number = models.CharField(max_length=100)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.Fullname

class Nurse(models.Model):
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50)
    Contact_Number = models.CharField(max_length=100)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.Fullname 
    
class OutPatient(models.Model):
    id = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=225)
    Gender = models.CharField(max_length=20)
    Village =  models.CharField(max_length=250)
    diseases = models.CharField(max_length=255)
    visited = models.DateField(default=now)
    drugs = models.CharField(max_length=500)

class AdmittedPatient(models.Model):
    id =  models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=255)
    Gender = models.CharField(max_length=20)
    village = models.CharField(max_length=255)
    diseases = models.CharField(max_length=255)
    admitted = models.DateField(default=now)
    Bed_Number = models.CharField(max_length=5)
    drugs = models.CharField(max_length=500)



    

@receiver(post_save, sender=CustomUser)
def create_user(sender,instance,created, **kwargs):
    if created: 
        if instance.user == 1:
            Administrator.objects.create(admin=instance)
        if instance.user == 2:
            Doctor.objects.create(admin=instance)
        if instance.user == 3:
            Nurse.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)

def save_user(sender, instance, created, **kwargs):
    if created:
        if instance.user == 1:
            instance.administrator.save()
        if instance.user == 2:
            instance.doctor.save()
        if instance.user == 3:
            instance.nurse.save()



