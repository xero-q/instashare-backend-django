from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework_simplejwt.tokens import RefreshToken

class SignupViewTest(APITestCase):
    def test_signup(self):
        url = reverse('signup')  # assuming you have a URL route named 'signup'
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class FileUploadTest(APITestCase):
    def setUp(self):
        # Create user and obtain token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_file_upload(self):
        url = reverse('file-upload')  # assuming URL for file upload is 'file-upload'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        file = SimpleUploadedFile('test.txt', b'This is a test file.', content_type='text/plain')
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)