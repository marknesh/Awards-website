from django.test import TestCase
from .models import Profile,Projects


class ProfileTest(TestCase):

    def setUp(self):
        self.profile=Profile(profile_photo="dog.url",bio="awsome",username="nesh")


    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))


class ProjectTest(TestCase):

    def setUp(self):
        self.project=Projects(project_name="github",project_photo="github.url",project_description="awsome stuff",project_link="github.com",pub_date="2020-09-23")


    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))

# Create your tests here.
