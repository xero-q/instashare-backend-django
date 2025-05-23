from django.urls import path

from .views import create_person

urlpatterns = [
    path("post", create_person, name="create-person")
]
