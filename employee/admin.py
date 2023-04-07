from django.contrib import admin

# Models
from employee.models import EmployeeInfo
from employee.models import DesignationInfo


# Register your models here.
@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display=('employee_of','position','employee_id','phone')
    search_fields=('employee_id','phone')
    list_per_page=50


@admin.register(DesignationInfo)
class DesignationAdmin(admin.ModelAdmin):
    list_display=('designation','department','created_at','updated_at')
    search_fields=('designation','department')
    list_per_page=50

