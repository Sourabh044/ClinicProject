from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Patient, Appointment
widgets = {
      'bdate' : forms.SelectDateWidget(),         
      }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')
        exclude = ['date_recorded', 'user']

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop user from kwargs
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user:
            # Filter the queryset based on the current user
            self.fields['patient'].queryset = Patient.objects.filter(user=user)


    class Meta:
        model = Appointment
        fields = ('__all__')
        exclude = ['approved', 'name', ]
