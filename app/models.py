from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_lastname = models.CharField(max_length=30)
    gpa = models.FloatField()
    
    def __str__(self):
        return self.student_name


