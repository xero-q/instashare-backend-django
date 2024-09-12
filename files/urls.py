from django.urls import path
from .views import SignupView, FileUploadView, FileUploadByIdView, FilesView, FileView

urlpatterns = [
    path('auth/signup', SignupView.as_view(), name='signup'),  
    path('api/files',FilesView.as_view(), name='file-list'),
    path('api/files/<int:pk>',FileView.as_view(), name='file-get'),
    path('api/upload', FileUploadView.as_view(), name='file-upload'),
    path('api/upload/<int:pk>', FileUploadByIdView.as_view(), name='file-rename'),
]