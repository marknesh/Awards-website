from django.test import TestCase
from .models import Profile


class ImageTest(TestCase):

    def setUp(self):
        self.profile=Profile(profile_photo="fff",bio="VV",username="DD")


    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

# Create your tests here.
