from django import forms
from .models import Image,Profile,Comments

class ProfileForm(forms.Form):
  
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    prof_image = forms.ImageField(upload_to='images/')
    bio = forms.CharField(max_length =200)

class ImageForm(forms.Form):
    
    image = forms.ImageField(upload_to='images/')
    name = forms.CharField(max_length =60)
    caption = forms.CharField(max_length =200)

class CommentsForm(forms.Form):

    comment = forms.CharField(max_length = 300)
    