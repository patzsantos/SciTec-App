"""This will load the page that contains the ISS parameters and range.
Encryption of the environment was referenced from:
Circumeo (2023) Encrypting Data in a Django Application.
Available from: https://circumeo.io/blog/entry/encrypting-data-in-a-django-application/
[Accessed 26 May 2024]"""

from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


# ranges are: "below range, normal range, and above range"
class Range(models.Model):
    Range = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.Range


# environment has the ISS cabin parameters checked by SciTec
class Environment(models.Model):
    objects = None
    # parameters are: oxygen level, cabin pressure, and cabin temperature
    Parameters = EncryptedCharField(max_length=30, default='')
    # addition date and changes are kept in history
    date_added = models.DateField(auto_now_add=True)
    # checks what range the parameter is in
    Range = models.ForeignKey(Range, on_delete=models.CASCADE)

    def __str__(self):
        return self.Parameters
