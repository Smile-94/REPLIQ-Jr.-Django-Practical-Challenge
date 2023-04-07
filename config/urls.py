
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include

# Yet another Swagger generator
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Apps Urls
from accounts import urls as accounts_urls
from employee import urls as employee_urls
from assests import urls as assests_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assests/v1/', include(accounts_urls)),
    path('assests/v1/', include(employee_urls)),
    path('assests/v1/', include(assests_urls)),
]

#JWT Tocken path
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#Yet another Swagger generator
schema_view = get_schema_view(
   openapi.Info(
      title="REPLIQ-Jr.-Django-Practical-Challenge",
      default_version='v1',
      description="""to track corporate assets such as phones, tablets, laptops 
        and other gears handed out to employees.""",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mshossen75@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
