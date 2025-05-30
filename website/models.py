from django.db import models

# Create your models here.

# student model
class Student(models.Model):
    user_id=models.CharField(max_length=50)
    student_name =models.CharField(max_length=50),
    college_code=models.CharField(10),
    college_name=models.CharField(max_length=50),
    branch_name=models.CharField(max_length=50),
    district=models.CharField(max_length=50),
    university=models.CharField(max_length=50)

