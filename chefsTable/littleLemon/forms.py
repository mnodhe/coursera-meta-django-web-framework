from django import forms
from django.forms import NumberInput


SHIFTS = [
    {'1', 'Morning'},
    {'2', 'Afternoon'},
    {'3', 'Evening'},
]


class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text="Enter the exact time")
    # reservation_date = forms.CharField(
    #     widget=NumberInput(attrs={'type': 'date'}))
