from django import forms 
from appointment.models import DayTime


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = DayTime
        fields = '__all__'
