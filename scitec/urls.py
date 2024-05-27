""" Code to change default Django header, index, and site
titles were taken from Gregory & sunwarr10r. (2019)
How to change site title, site header and index title
in Django Admin?.
Available from: https://stackoverflow.com/a/36251770
[Accessed 25 May 2024]."""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # leads to http://127.0.0.1:8000/
    path('', admin.site.urls),
    # leads to http://127.0.0.1:8000/cabin/
    path('cabin/', include('cabin.urls'))
]

admin.site.site_header = 'SciTec App'
admin.site.index_title = 'ISS Cabin Environment Parameter Checking'
admin.site.site_title = 'SciTec'
