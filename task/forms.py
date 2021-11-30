from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from .models import Task
import secrets, datetime
        
class TaskForm(forms.ModelForm):

    password        = forms.CharField(max_length=24, widget=forms.PasswordInput())
    confirm         = forms.CharField(max_length=24, widget=forms.PasswordInput())
    date_opening    = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time      = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time        = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Task
        fields = ['name', 'password', 'confirm', 'date_opening', 'start_time', 'end_time']

    def clean_date_opening(self):
        if self.cleaned_data['date_opening'] >= datetime.datetime.today().date():
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
