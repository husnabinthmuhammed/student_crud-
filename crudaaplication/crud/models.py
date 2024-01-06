from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    place = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name




