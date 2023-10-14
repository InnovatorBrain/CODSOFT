from django.urls import path
from .views import PasswordGenerator, GeneratedPasswordList

urlpatterns = [
    path('generate/<int:length>/', PasswordGenerator.as_view(), name='generate-password'),
    path('generated-passwords/', GeneratedPasswordList.as_view(), name='generated-password-list'),
]
