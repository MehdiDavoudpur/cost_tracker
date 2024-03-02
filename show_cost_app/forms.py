from django import forms
from .models import CostShow


class CostShowForm(forms.ModelForm):
    class Meta:
        model = CostShow
        fields = ['show']
