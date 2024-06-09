from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=100, blank=True)
    roll_number = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=255, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    otp = models.CharField(max_length=10, default="000000")

    def __str__(self):
        return self.email

class Teacher(models.Model):
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=100, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    otp = models.CharField(max_length=10, default="000000")
    def __str__(self):
        return self.email


class Club(models.Model):  
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):  
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
