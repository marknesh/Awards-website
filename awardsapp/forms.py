from django import forms

class ProfileUpdateForm(forms.Form):
    '''
    class that creates profile update form
    '''
    username = forms.CharField(label='Username',max_length = 30)
    profile_photo = forms.ImageField(label = 'Profile Photo')
    bio = forms.CharField(label='Bio',max_length=500)


class ProjectForm(forms.Form):
    '''
    class that creates project form
    '''
    project_name = forms.CharField(label='project name',max_length = 30)
    project_photo = forms.ImageField(label = 'Profile Photo')
    project_link = forms.CharField(label='project link', max_length=30)
    project_description = forms.CharField(label='Project description',max_length=500)