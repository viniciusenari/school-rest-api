from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    birthday = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )
    course_id = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description