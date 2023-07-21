from django.db import models
import string, random
from program.department import Department
from django.conf import settings


# Create your models here.


class Program(models.Model):
    LEVEL_CHOICE = [
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('Graduant', 'Graduant')
    ]
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True, choices=LEVEL_CHOICE)

    def __str__(self):
        return self.name


class Course(models.Model):
    SEMESTER_CHOICE = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2')
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=100, blank=True, null=True, choices=SEMESTER_CHOICE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    credit = models.IntegerField(null=True, blank=True)
    Grade = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    mark = models.CharField(max_length=100, null=True, blank=True)
    gpa = models.CharField(max_length=100, null=True, blank=True)
    course_code=models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='Not Registered')
    date_registered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        characters = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(characters) for _ in range(3))
        random_code += ''.join(random.choice(string.digits) for _ in range(3))
        self.course_code = random_code
        super().save(*args, **kwargs)

    
    def __str__(self):
        return str(self.name)
