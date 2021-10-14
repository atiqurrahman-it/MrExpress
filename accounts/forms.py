from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from userApp.models import User


# class RegisterCreateUserForm(UserCreationForm) Or :

# if {{forms.email}}
class RegisterCreateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email ', 'type': 'email', }))

    password = forms.CharField(required=True,
                               label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password '}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password','password2')

        widgets = {
                    'first_name': forms.TextInput(attrs={'placeholder': 'First Name ',
                                                            'class': 'form-control'}),
                    'last_name': forms.TextInput(attrs={'placeholder': 'Last Name ',
                                                            'class': 'form-control'}),
                }

# second way
# if {{forms}}
# class RegisterCreateUserForm(UserCreationForm):
#     email = forms.EmailField(required=True, label="",
#                              widget=forms.TextInput(attrs={'placeholder': 'Email ', 'type': 'email', }))
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name',
#                   'last_name', 'password1','password1']
#         widgets = {
#             'password1': forms.PasswordInput(attrs={'placeholder': 'Enter New Password',
#                                                     'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Repeat password',
#                                                     'class': 'form-control'}),
#         }


# if {{forms}}

# class RegisterCreateUserForm(UserCreationForm):
#     email = forms.EmailField(required=True, label="",
#                              widget=forms.TextInput(attrs={'placeholder': 'Email ', 'type': 'email', }))
#
#     password1 = forms.CharField(required=True,
#                                 label='',
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#     password2  = forms.CharField(required=True,
#                                 label='',
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))
#
#
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email', 'password1','password2')
#
