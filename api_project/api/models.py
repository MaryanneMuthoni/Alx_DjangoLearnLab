from django.db import models

# Create your models here.
class Student(models.Model):
    '''Class representing student instance'''
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    GENDER = [
            ('M', 'Male'), 
            ('F', 'Female'),
            ('O', 'Other'),
            ]

    gender = models.CharField(max_length=1, choices=GENDER, blank=False, null=False)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    grade = models.IntegerField()
    teacher = models.CharField(max_length=100)

    class Meta:
        ordering = ['grade', 'first_name']

class Book(models.Model):
    '''Class representing book instance'''
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
