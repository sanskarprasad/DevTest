from django.urls import path
from .views import home_view, file_upload_view

urlpatterns = [
    path('', home_view, name='home'),  # This will render the home page with the upload form
    path('upload/', file_upload_view, name='file_upload'),  # This will handle the file upload
]
