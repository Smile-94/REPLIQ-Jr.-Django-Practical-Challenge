from rest_framework.routers import DefaultRouter
from django.urls import path
from django.urls import include

# Import views
from accounts.views import manage_accounts

router = DefaultRouter()
router.register(r'users', manage_accounts.AccountsView)
router.register(r'profiles', manage_accounts.ProfileView)

app_name = 'accounts'

urlpatterns = [
    path('', include(router.urls)),
]
