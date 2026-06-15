from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from.models import Profile

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class':'formcontrol',
            'placeholder':'Could not be similar to User Name'
        })
        self.fields['password2'].widget.attrs.update({
            'class':'formcontrol',
            'placeholder':'Re-enter your Password'
        })

        
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        labels={
            'username':'User Name',
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email Address',
            'password1':'Create Password',
            'password2':'Confirm Password'
        }
        widgets={
            'username':forms.TextInput(attrs={
                'class':'formcontrol',
                'placeholder':'User Name must be unique.'
            }),
            'email':forms.TextInput(attrs={
                'class':'formcontrol',
                'placeholder':'Only Gmail addresses are allowed.'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'formcontrol',
            }),
            'last_name':forms.TextInput(attrs={
                'class':'formcontrol',
            })
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']




class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'formcontrol'})
        self.fields['password'].widget.attrs.update({'class':'formcontrol'})

    error_messages={
        'invalid_login':'Invalid Username Or Password',
        'inactive':'This Account IS Inactive'
    }