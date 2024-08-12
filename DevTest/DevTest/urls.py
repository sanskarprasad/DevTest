from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('fileupload.urls')),  # Including the URLs from the fileupload app for the home page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
