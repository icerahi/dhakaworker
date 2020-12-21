from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from apps.accounts.models import WorkerProfile


class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control',
                                             'placeholder':'username'})
        self.fields['email'].widget.attrs.update({'class':'form-control',
                                            'placeholder':'email'}),
        self.fields['password1'].widget.attrs.update({'class':'form-control',
                                               'placeholder':'password'}),
        self.fields['password2'].widget.attrs.update({'class' :'form-control',
                                               'placeholder':'confirm password'})

class ProfileForm(ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ("image","fullname","category","working_time","hourly_rate","working_area","extra_service",
                 "experience","phone",)

    def __init__(self,*args,**kwargs):
        super(ProfileForm, self).__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control',
                                             'placeholder':'image'})
        self.fields['fullname'].widget.attrs.update({'class':'form-control',
                                            'placeholder':'category'}),
        self.fields['working_time'].widget.attrs.update({'class':'form-control',
                                               'placeholder':'working_time'}),
        self.fields['hourly_rate'].widget.attrs.update({'class' :'form-control',
                                               'placeholder':'hourly_rate'})
        self.fields['working_area'].widget.attrs.update({'class' :'form-control',
                                               'placeholder':'working_area'})

        self.fields['extra_service'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'extra_service'})
        self.fields['experience'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'experience'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control',
                                                     'placeholder': 'phone'})
