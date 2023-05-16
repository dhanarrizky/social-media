from typing import Any
from django import forms
from .models import Meep, Profile

# for create form views from django auth form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# created user interface used to form.py
class MeepForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget =forms.widgets.Textarea(
            attrs={
                "placeholder":"Enter Your Musker Meep !!",
                "class":"form-control",
                }), label="",
    )
    
    class Meta:
        model = Meep
        exclude = ("user",'likes')
        

class UserSignUp(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"email address"}))
    first_name = forms.CharField(label='',max_length=200, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"first name"}))
    last_name = forms.CharField(label='',max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    #username = forms.CharField(label='',max_length=200, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"username"}))
    #password1 = forms.CharField(label='',max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password 1'}))
    #password2 = forms.CharField(label='',max_length=200, widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"password 2"}))
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1', 'password2']
    
    
    def __init__(self, *args, **kwargs):
        super(UserSignUp, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].label=''
        #self.fields['username'].help_text=
    
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='password1'
        self.fields['password1'].label=''
        #self.fields['username'].help_text=
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='password2'
        self.fields['password2'].label=''
        #self.fields['username'].help_text=
        
        
# create profile picture form
class ProfilePicForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='Profile Picture')
        

    class Meta:
        model = Profile
        fields = ('profile_pic',)
