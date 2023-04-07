from django.db import models
import datetime

# Models
from accounts.models import User

# Create your models here.
DEPARTMENT_OPT = (
    ('HR', 'Human Resource'),
    ('administrative', 'Administrative'),
    ('software development', 'Software Development'),
    ('QA', 'Quality Assurance'),
    ('project management', 'Project Management'),
    ('product panagement', 'Product Management'),
    ('design', 'Design'),
    ('devOps', 'DevOps'),
    ('customer support', 'Customer Support'),
    ('marketing', 'Marketing'),
    ('IT', 'Information Technology')
)
# To add dynamitically add designation
class DesignationInfo(models.Model):
    designation_of = models.ForeignKey(User, related_name='designation_of', on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_OPT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.designation}, {self.department}"

class EmployeeInfo(models.Model):
    employee_of = models.ForeignKey(User, related_name='employee_company', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True)
    position = models.ForeignKey(DesignationInfo, on_delete=models.SET_NULL, blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15)
    national_id = models.CharField(max_length=50)
    photo = models.ImageField(blank=True)
    signature = models.ImageField(blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.employee_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.employee_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
        
    def __str__(self):
        return str(self.full_name)
