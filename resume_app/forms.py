from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'job_experience', 'skills', 'education')


