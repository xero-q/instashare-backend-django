from django.urls import path
from .views import SignupView, FileUploadView, FileUploadByIdView

urlpatterns = [
    path('auth/signup', SignupView.as_view(), name='signup'),
    path('api/upload', FileUploadView.as_view(), name='file-upload'),
    path('api/upload/<int:pk>', FileUploadByIdView.as_view(), name='file-rename'),
]