"""OpenAI Language Model ChatGPT 3.5 was used to assist in writing this code,
while also referring to Ridgway, A. (2021) Django Testing for Beginners.
Available from:
https://alicecampkin.medium.com/django-testing-for-beginners-146bd285a178
[Accessed 25 May 2024].
Modifications were made by the developer accordingly."""


from django.urls import reverse
from django.test import TestCase


# tests that when running the server, the user is lead to the SciTec login page
class TestSciTecUrl(TestCase):
    def test_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/', 201)
