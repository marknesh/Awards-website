from rest_framework import serializers
from .models import Profile,Projects

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio', 'username')


class MerchSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_name', 'project_photo', 'project_description','project_link')