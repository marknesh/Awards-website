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

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30,null=True)
    option_two = models.CharField(max_length=30,null=True)
    option_three = models.CharField(max_length=30,null=True)
    option_four= models.CharField(max_length=30,null=True)
    option_five = models.CharField(max_length=30 ,null=True)
    option_six= models.CharField(max_length=30,null=True)
    option_seven = models.CharField(max_length=30,null=True)
    option_eight = models.CharField(max_length=30,null=True)
    option_nine = models.CharField(max_length=30,null=True)
    option_ten= models.CharField(max_length=30,null=True)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    option_five_count = models.IntegerField(default=0)
    option_six_count = models.IntegerField(default=0)
    option_seven_count= models.IntegerField(default=0)
    option_eight_count = models.IntegerField(default=0)
    option_nine_count = models.IntegerField(default=0)
    option_ten_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count + self.option_six_count + self.option_seven_count+ self.option_nine_count + self.option_ten_count

class Projects(models.Model):
    project_photo=models.ImageField(upload_to='projectpics/')
    project_description=HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    project_name = models.CharField(max_length=30,default='User')
    project_link = models.CharField(max_length=100,default='User')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()



    @classmethod
    def search_project(cls, name):
        search = cls.objects.filter(project_name__icontains=name)
        return search

    def get_project(cls,po):
        gett=cls.objects.filter(id=po)
        return gett

