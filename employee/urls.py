from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include

# Views
from employee.views import manage_designation

router = DefaultRouter()
router.register(r'designations', manage_designation.DesignationView)

app_name = 'employee'

urlpatterns = [
    path('', include(router.urls)),
]
