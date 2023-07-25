from django.test import TestCase

# Create your tests here.
from .models import User,SoundList
from django.test import TestCase


class MyTestCase(TestCase):
    def test_models():
        print(SoundList.objects.all())
    