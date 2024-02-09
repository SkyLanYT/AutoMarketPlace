from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Advertisement


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        error_messages = {
            'password_mismatch': "Паролі не співпадають.",
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'price', 'description', 'photo1', 'photo2', 'photo3', 'number_phone']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-class', 'placeholder': 'Введіть назву оголошення'}),
            'price': forms.TextInput(attrs={'class': 'form-class', 'placeholder': 'Введіть ціну оголошення'}),
            'description': forms.TextInput(attrs={'class': 'form-class', 'placeholder': 'Введіть опис оголошення'}),
            'photo1': forms.FileInput(attrs={'class': 'form-class', 'accept': 'image/*'}),
            'photo2': forms.FileInput(attrs={'class': 'form-class', 'accept': 'image/*'}),
            'photo3': forms.FileInput(attrs={'class': 'form-class', 'accept': 'image/*'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-class', 'placeholder': 'Введіть ваш номер телефону: +380'})
        }