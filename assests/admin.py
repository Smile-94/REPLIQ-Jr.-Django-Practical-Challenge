from django.contrib import admin

# Models
from assests.models import Assests 
from assests.models import HandedOutAssests

# Register your models here.
@admin.register(Assests)
class AssestsAdmin(admin.ModelAdmin):
    list_display = ('assests_of','assests_name','assests_type','assests_id')
    search_fields = ('assests_of','assests_id')
    list_filter = ('assests_type',)
    list_per_page = 50

@admin.register(HandedOutAssests)
class HandedOutAssests(admin.ModelAdmin):
    list_display = ('handedout_by','handedout_to','product','issued_id')
    search_fields = ('issued_id',)
    list_per_page = 50

