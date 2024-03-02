from django import forms
from .models import CostEntry


class CostEntryForm(forms.ModelForm):
    class Meta:
        model = CostEntry
        fields = ['date', 'cost_for', 'cost_group', 'price']
        widgets = {
                    'date': forms.DateInput(attrs={'type': 'date'})
                }