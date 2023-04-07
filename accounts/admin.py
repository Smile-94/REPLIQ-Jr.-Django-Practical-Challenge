from django.contrib import admin

# models
from accounts.models import User
from accounts.models import Profile


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('email','is_clients','is_staff','is_active')
    search_fields=('email',)
    list_per_page=50

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','company_name','company_type','city','zip_code','country')
    search_fields=('user','company_name','company_type')
    raw_id_fields=('user',)
    list_per_page=50