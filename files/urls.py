from django.urls import path
from .views import SignupView, FileUploadView, FileUpdateByIdView, FilesView, download_file

urlpatterns = [
    path('auth/signup', SignupView.as_view(), name='signup'),  
    path('api/files',FilesView.as_view(), name='file-list'),
    path('api/download/<int:pk>',download_file, name='file-download'),
    path('api/upload', FileUploadView.as_view(), name='file-upload'),
    path('api/update/<int:pk>', FileUpdateByIdView.as_view(), name='file-rename'),
]