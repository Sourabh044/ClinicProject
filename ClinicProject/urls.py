from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomePage.urls')),
    path('User/', include('django.contrib.auth.urls')),
    # path('Appointment/', include('Appointment.urls')),
]
