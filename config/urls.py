
from django.contrib import admin
from django.urls import path
from django.urls import include


# Apps Urls
from accounts import urls as accounts_urls
from employee import urls as employee_urls
from assests import urls as assests_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assests/v1/', include(accounts_urls)),
    path('assests/v1/', include(employee_urls)),
    path('assests/v1/', include(assests_urls)),
]
