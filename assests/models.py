from django.db import models
import datetime

# Modesl
from accounts.models import User
from employee.models import EmployeeInfo

# phones, tablets, laptops 
ASSESTS_OPT = (
    ('phones','Phones'),
    ('tablets','laptops'),
    ('laptop','laptop'),
)

# Create your models here.
class Assests(models.Model):
    assests_of = models.ForeignKey(User, related_name='assests', on_delete=models.CASCADE)
    assests_name = models.CharField(max_length=50)
    assests_type = models.CharField(max_length=15,choices=ASSESTS_OPT)
    assests_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    # This function will automatically create assests id and save 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.assests_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.assests_id = 'ASS'+year+month+day+str(self.pk).zfill(4)
            self.save()

    def __str__(self):
        return self.assests_name

class HandedOutAssests(models.Model):
    handedout_by = models.ForeignKey(User, related_name='handedout_by', on_delete=models.CASCADE)
    handedout_to = models.ForeignKey(EmployeeInfo, on_delete=models.CASCADE)
    product = models.ForeignKey(Assests,on_delete=models.CASCADE, related_name='assests')
    issued_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    provide_at = models.DateField(auto_now_add=True)
    return_at = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    present_condition = models.TextField()
    return_condition = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    # This function will automatically create issued id and save 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.issued_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.issued_id = 'HND'+year+month+day+str(self.pk).zfill(4)
            self.save()

    def __str__(self):
        return str(self.product)
    
