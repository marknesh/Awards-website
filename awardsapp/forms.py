from django import forms

class ProfileUpdateForm(forms.Form):
    '''
    classs that creates profile update form
    '''
    username = forms.CharField(label='Username',max_length = 30)
    profile_photo = forms.ImageField(label = 'Profile Photo')
    bio = forms.CharField(label='Bio',max_length=500)