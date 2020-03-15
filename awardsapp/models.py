from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profilepics/')
    bio=HTMLField()
    username = models.CharField(max_length=30,default='User')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Projects(models.Model):
    project_photo=models.ImageField(upload_to='projectpics/')
    project_description=HTMLField()
    project_name = models.CharField(max_length=30,default='User')
    project_link = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()