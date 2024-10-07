from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer,
    UploadedFileSerializer,
    CustomTokenObtainPairSerializer,
)
from .models import UploadedFile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.decorators import api_view
import os


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FilesPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "perPage"
    max_page_size = 100


class FilesView(generics.ListAPIView):
    queryset = UploadedFile.objects.all().order_by("id")
    serializer_class = UploadedFileSerializer
    pagination_class = FilesPagination


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = FilesPagination

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES["file"]
        status_file = (
            "compressed" if uploaded_file.name.endswith(".zip") else "uploaded"
        )
        file_instance = UploadedFile.objects.create(
            file=uploaded_file,
            name=uploaded_file.name,
            size=uploaded_file.size,
            status=status_file,
        )
        serializer = UploadedFileSerializer(file_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileUpdateByIdView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            uploaded_file = UploadedFile.objects.get(pk=pk)
            name = request.data.get("name")

            SEPARATOR = "/"

            file_real_name = uploaded_file.file.name.split(SEPARATOR)[-1]

            original_name_path = os.path.join(
                settings.BASE_DIR, settings.UPLOADS_FOLDER, file_real_name
            )
            new_name_path = os.path.join(
                settings.BASE_DIR, settings.UPLOADS_FOLDER, name
            )
            os.rename(original_name_path, new_name_path)

            uploaded_file.name = name

            file_name_array = uploaded_file.file.name.split(SEPARATOR)
            file_name_array[-1] = name
            uploaded_file.file.name = SEPARATOR.join(file_name_array)

            uploaded_file.save()
            serializer = UploadedFileSerializer(uploaded_file)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UploadedFile.DoesNotExist:
            return Response(
                {"error": "File not found"}, status=status.HTTP_404_NOT_FOUND
            )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view()
def download_file(request, pk):
    # Fetch the file object
    file_obj = get_object_or_404(UploadedFile, pk=pk)

    SEPARATOR = "/"

    file_real_name = file_obj.file.name.split(SEPARATOR)[-1]

    file_path = os.path.join(settings.BASE_DIR, settings.UPLOADS_FOLDER, file_real_name)

    try:
        with open(file_path, "rb") as file:
            response = HttpResponse(
                file.read(), content_type="application/octet-stream"
            )
            response["Content-Disposition"] = (
                f"attachment; filename={smart_str(file_real_name)}"
            )
            return response
    except FileNotFoundError:
        raise Http404("File does not exist")
