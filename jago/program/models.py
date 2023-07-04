from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)


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
	

class Course(models.Model):
   
	SEMESTER_CHOICE= [
		('Semester 1', 'Semester 1'),
		('Semester 2', 'Semester 2')
	]
	name = models.CharField(max_length=100, blank=True, null=True)
	semester = models.CharField(max_length=100, blank=True, null=True, choices=SEMESTER_CHOICE)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	