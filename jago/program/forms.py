from django import forms
from program.models import Course



class RegistrationHistoryForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['semester', 'year']