from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('addresses.urls'))  # Will be able to urls in a file called address.urls.py
]
