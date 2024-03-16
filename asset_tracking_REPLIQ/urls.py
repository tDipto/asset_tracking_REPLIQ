from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    # path('', admin.site.urls),
    path('admin/', admin.site.urls),
    
    path("api/v1/companies/", include("Company.urls")),
    # path("api/v1/devices/", include("Device.urls")),
    path("api/v1/employees", include("Employee.urls")),
    # path("api/v1/tracking", include("Tracking.urls")),
]
