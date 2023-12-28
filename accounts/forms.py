from django import forms
from .models import CustomUser,Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+("is_artist",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['user','photo']



class LoginForm(forms.Form):
    username=forms.CharField(max_length=65, widget=forms.TextInput(attrs={
        'placeholder':'Enter username',
        'class':'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
    }))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500'
    }))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

        def clean_password(self):
            cd=self.cleaned_data
            if cd['password2']!= cd['password1']:
                raise forms.ValidationError('Password did\'t match')
            return cd['password2']
        def clean_email(self):
            data=self.cleaned_data['email']
            qs=User.objects.exclude(id=self.instance.id).filter(email=data)
            if qs.exists():
                raise forms.ValidationError('Email already in use')
            return data
        
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your Username',
        'class':''
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter email address',
        'class':''
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':''
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':''
    }))
