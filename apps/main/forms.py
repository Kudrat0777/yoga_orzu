from dataclasses import field
from pyexpat import model
from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'