from django.db import models
# from.models import baseModel
# from django import Department


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
    



















# class customersModel(baseModel):
#     customer_id = models.CharField(primary_key=True,max_length=255, blank=True)
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
#     email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
#     mobile = models.CharField(max_length=255, blank=True)
#     password = models.CharField(max_length=255)
#     is_activate = models.BooleanField(default=False)
#     is_added_address = models.BooleanField(default=False)
#     otp = models.CharField(max_length=10, default="111111")

#     def __str__(self):
#         return f"{self.customer_id} - {self.first_name} {self.last_name}"

#     def save(self, *args, **kwargs):
#         if not self.customer_id:
#             self.customer_id = self.generate_customer_id()
#         return super(customersModel, self).save(*args, **kwargs)
    
#     def generate_customer_id(self):
#         last_customer = customersModel.objects.order_by('-customer_id').first()
#         if last_customer:
#             last_id = int(last_customer.customer_id[3:])  # Extracting the numeric part
#             new_id = last_id + 1
#         else:
#             new_id = 1
#         return 'CUM{:04d}'.format(new_id)
    

# class customerAddressModel(baseModel):
    # customer_id = models.ForeignKey(customersModel, on_delete=models.CASCADE)
    # street_address = models.CharField(max_length=255)
    # city = models.CharField(max_length=255)
    # pincode = models.CharField(max_length=255)
    # state = models.CharField(max_length=255)