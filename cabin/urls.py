""" URLs that lead to the range and environment pages in the SciTec App"""

from django.urls import path
from .views import RangeList, EnvironmentList


urlpatterns = [
    path('range/', RangeList.as_view(), name='range'),
    path('environment/', EnvironmentList.as_view(), name='environment'),
]