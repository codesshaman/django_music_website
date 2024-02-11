from .views import FileUploadAPIView
from django.urls import path
from .views import music
from .views import home



urlpatterns = [
    path('api/music/', music, name='music'),
    path('api/upload/', FileUploadAPIView.as_view(), name='file_upload'),
    path('', home)
]
