from django import forms
from django.db.models import fields
from . import models

class CRUDform(forms.ModelForm):
    class Meta:
        model = models.CRUDfunctions
        fields=["title","description"]