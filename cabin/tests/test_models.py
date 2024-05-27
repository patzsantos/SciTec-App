"""OpenAI Language Model ChatGPT 3.5 was used to assist in writing this code,
while also referring to Ridgway, A. (2021) Django Testing for Beginners.
Available from:
https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178
[Accessed 25 May 2024].
Modifications were made by the developer accordingly."""

from django.test import TestCase
from cabin.models import Range, Environment


# tests range models, and gets their position in the list.
class TestRange(TestCase):
    @classmethod
    def setUpTestData(cls):
        Range.objects.create(Range='Range')

    def TestRange(self):
        range_list = Range.objects.get(id=1)
        self.assertEqual(range_list.__str__(), 'Range')


# tests environment models, and gets their position in the list.
class TestEnvironment(TestCase):
    @classmethod
    def setUpTestData(cls):
        Range.objects.create(Range='Range')
        Environment.objects.create(Parameters='Parameters', Range_id=1)

    def TestEnvironment(self):
        environment_list = Environment.objects.get(id=1)
        self.assertEqual(environment_list.__str__(), 'Parameters')
