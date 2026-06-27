from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, ServiceRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message...', 'rows': 5, 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff; resize: none;'}),
        }

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone', 'service', 'budget', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'service': forms.Select(attrs={'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Your Budget (e.g. 5000 PKR)', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your project in detail...', 'rows': 4, 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff; resize: none;'}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose Username', 'style': 'width: 100%; padding: 14px 16px; border: 2px solid #e8f0fe; border-radius: 12px; font-size: 14px; font-family: Poppins, sans-serif; outline: none; background: #f8faff;'}),
        }