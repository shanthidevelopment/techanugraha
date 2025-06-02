from django.db import models

class Student(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    student_name = models.CharField(max_length=100)
    college_code = models.CharField(max_length=20)
    college_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.student_name


class CourseProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_progress')
    course_id = models.CharField(max_length=100)
    course_unique_code = models.CharField(max_length=100)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    certificate_issued = models.BooleanField(default=False)
    assessment_status = models.BooleanField(default=False)
    course_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.student_name} - {self.course_id}"
