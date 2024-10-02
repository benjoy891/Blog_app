from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

common_attrs = {
    'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-500 !important',
}

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            **common_attrs,
            'placeholder': 'Email Address'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                **common_attrs,
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                **common_attrs,
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                **common_attrs,
                'placeholder': 'Confirm Password'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-500 transition duration-200 ease-in-out',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-md p-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-500 transition duration-200 ease-in-out',
                'placeholder': 'Email Address'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'border border-gray-300 rounded-md p-3 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out'
            }),
        }