from django.contrib.auth.models import User
from django import forms
from phone_field import PhoneField
from django_countries.fields import CountryField
from django.contrib.auth.forms import UserCreationForm

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ['username','email','password']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1')

# class ArtistForm(forms.ModelForm):
#     Mobile_Number = PhoneField(blank=True, help_text='Contact phone number')
#     country = CountryField(default="India")
#     desc = models.TextField(blank=True, null=True)
#     password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model =
    #     fields = ('username','email', 'password','Mobile_Number','country','desc')
