from django.db import models

# Create your models here.

class Faculty(models.Model):
    #Se crea una clase llamda Faculty equivale a una tabla en el modelo
    faculty_id = models.CharField(max_length=10, primary_key=True)
    faculty_name = models.CharField(max_length=200)
    faculty_description = models.TextField()
    faculty_image = models.ImageField(
        upload_to='faculties/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.faculty_id


class Department(models.Model):
    department_id = models.CharField(max_length=5, primary_key=True)
    department_name = models.CharField(max_length=200)
    faculty  = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_id


class Program(models.Model):
    program_id = models.CharField(max_length=10, primary_key=True)
    program_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.program_id


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, primary_key=True)
    teacher_name = models.CharField(max_length=100, null=False)
    teacher_email = models.EmailField(null=True)
    teacher_phone = models.CharField(max_length=10)
    teacher_gender = models.CharField(max_length=2)
    teacher_age = models.PositiveIntegerField()
    teacher_height = models.DecimalField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_id



