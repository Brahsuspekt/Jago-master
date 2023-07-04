from django.db import models
from django.contrib.auth.models import User 
from program.models import Program, Department

class CustomUser(User):
    QUAL_CHOICES = [
        ('wassce', 'wassce'),
        ('degree', 'degree'),
        ('masters', 'masters'),
        ('doctorate', 'doctorate'),
        ('professor', 'professor')
    ]
    dob = models.DateField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(Program,on_delete=models.SET_NULL, null=True, blank=True)
    qualification = models.CharField(choices=QUAL_CHOICES, max_length=100, blank=True, null=True)
    is_lecturer = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}"
