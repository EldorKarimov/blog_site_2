from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="parol kiriting:",
                                widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'parol kiriting'}))
    password2 = forms.CharField(label="parol qayta kiriting:",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'parol qayta kiriting'}))
    first_name = forms.CharField(label="ismingizni kiriting:",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'your name'}))
    last_name = forms.CharField(label="familiyangizni kiriting:",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'your last name'}))
    date_of_birth = forms.CharField(label="tug'ilgan sanangizni kiriting:",
                                widget=forms.DateInput(
                                    attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'email', 'date_of_birth', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'username kiriting:'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email kiriting:'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'telefon raqam kiriting:'}),
            # 'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'})
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'image', 'addres']