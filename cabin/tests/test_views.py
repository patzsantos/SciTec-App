""" Code based on Lorenz, T. (2019) Proper Unit Tests for Your Django Views.
Available from:
https://blog.bitlabstudio.com/proper-unit-tests-for-your-django-views-b4a1730a922e
[Accessed on 25 May 2024]."""

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from cabin import views


# tests that 'range/' leads to the 'Cabin Administration' page
class CabinAdministrationTest(TestCase):
    longMessage = True

    def TestGetEnvironmentList(self):

        req = RequestFactory().get('range/')
        req.user = User()
        resp = views.EnvironmentList.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, 200)


# tests that 'cabin/environment/' leads to 'Select environment to change' page
class SelectEnvironmentTest(TestCase):
    longMessage = True

    def TestGetRangeList(self):

        req = RequestFactory().get('cabin/environment/')
        req.user = User()
        resp = views.RangeList.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, 200)
