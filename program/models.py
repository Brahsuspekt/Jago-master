from django.db import models
import random 
import string

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Program(models.Model):
    LEVEL_CHOICE = [
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('Graduant', 'Graduant')
    ]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True, choices=LEVEL_CHOICE)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    SEMESTER_CHOICE = [
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
    ]
    course_code = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=100, blank=True, null=True, choices=SEMESTER_CHOICE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    credit = models.IntegerField(null=True, blank=True)
    Grade = models.CharField(max_length=100, null=True, blank=True)
    gpa = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        characters = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(characters) for _ in range(3))
        random_code += ''.join(random.choice(string.digits) for _ in range(3))
        self.course_code = random_code
        super().save(*args, **kwargs)
