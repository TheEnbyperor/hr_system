from django import forms
from . import models


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ('name',)
