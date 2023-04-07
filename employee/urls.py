from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include

# Views
from employee.views import manage_designation
from employee.views import manage_employee

# Router for the employee and designation view
router = DefaultRouter()
router.register(r'designations', manage_designation.DesignationView)
router.register(r'employees', manage_employee.EmployeeInfoView)

app_name = 'employee'

urlpatterns = [
    path('', include(router.urls)),
]
