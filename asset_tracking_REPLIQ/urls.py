from django.contrib import admin
from django.urls import include,path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    
    path("api/v1/companies/", include("Company.urls")),
    path("api/v1/devices/", include("Device.urls")),
    path("api/v1/employees/", include("Employee.urls")),
    path("api/v1/tracking/", include("Tracking.urls")),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
