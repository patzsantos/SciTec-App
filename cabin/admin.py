"""Admin can access range and environment fields in the SciTec App"""

from django.contrib import admin
from cabin.models import Range, Environment


# registered admin can access the ISS cabin environment and the range
admin.site.register(Range)
admin.site.register(Environment)
