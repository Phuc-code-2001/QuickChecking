from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.conf import settings

from django.conf import settings
from .models import Task

import pytz

SERVER_TZ = pytz.timezone(settings.TIME_ZONE)
        
class TaskForm(forms.ModelForm):

    name            = forms.CharField(label="Topic", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password        = forms.CharField(max_length=24, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm         = forms.CharField(max_length=24, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    date_opening    = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    start_time      = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))
    end_time        = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['name', 'password', 'confirm', 'date_opening', 'start_time', 'end_time']

    def clean_date_opening(self):
        if self.cleaned_data['date_opening'] >= timezone.now().astimezone(SERVER_TZ).date():
            return self.cleaned_data['date_opening']
        raise ValidationError("Date opening must be equal or after today.")

    def clean_confirm(self):
        if self.cleaned_data['password'] == self.cleaned_data['confirm']:
            return self.cleaned_data['confirm']
        else:
            raise ValidationError("Confirm password incorrect.")

    def clean_end_time(self):
        if self.cleaned_data['start_time'] >= self.cleaned_data['end_time']:
            raise ValidationError("Start time must be before end time.")
        else:
            return self.cleaned_data['end_time']
