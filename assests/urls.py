from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include

# Views
from assests.views import manage_assests
from assests.views import manage_handedout

# Router for the assests and handedout assests view
router = DefaultRouter()
router.register(r'assestses', manage_assests.AssestsView)
router.register(r'handed_assestses', manage_handedout.HandedOutAssestsView)

app_name = 'assests'

urlpatterns = [
    path('', include(router.urls)),
]
