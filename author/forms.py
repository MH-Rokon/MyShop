from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
           
        
# form class to update the user  information    
class UserupdateFrom(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['first_name','last_name','email']
     
  
# form class to update the user profile information    
class UserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=Profile
        fields=['phone','address1','address2','city','state','zipcode','country']
        
              
# form class to update the user password   
class ChangePasswordForm(SetPasswordForm):
    password=None
    class Meta:
        model=User
        fields=['new_password1','new_password2']