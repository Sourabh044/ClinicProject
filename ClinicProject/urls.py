from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomePage.urls')),
    # path('Appointment/', include('Appointment.urls')),
]
