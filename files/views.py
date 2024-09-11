from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,UploadedFileSerializer
from .models import UploadedFile
from django.contrib.auth.models import User

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        print(f"User: {request.user}, Auth: {request.auth}")
        uploaded_file = request.FILES['file']
        file_instance = UploadedFile.objects.create(
            file=uploaded_file,
            original_name=uploaded_file.name,
            size=uploaded_file.size,
        )
        serializer = UploadedFileSerializer(file_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        files = UploadedFile.objects.all()
        serializer = UploadedFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            uploaded_file = UploadedFile.objects.get(pk=pk)
            new_name = request.data.get('new_name')
            uploaded_file.new_name = new_name
            uploaded_file.save()
            serializer = UploadedFileSerializer(uploaded_file)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UploadedFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)