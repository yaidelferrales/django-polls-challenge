import datetime
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise forms.ValidationError("password didn't match")
        return ['password2']
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
    
    def clean_date_of_birth(self):
        """between 6 and 94  years as limit"""
        data = self.cleaned_data["date_of_birth"]
        time_max = timezone.now() + datetime.timedelta(days=-2190)
        time_min = timezone.now() + datetime.timedelta(days=-36500)
        if not time_min.date() <= data <= time_max.date() :
            raise forms.ValidationError("The date of birth is not correct, please type the correct date")
        return data      
        
    