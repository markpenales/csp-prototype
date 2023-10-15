from django import forms

from playground.models import Instructor, Laboratory


class CreateScheduleForm(forms.Form):
    course = forms.CharField(max_length=255)

class SaveScheduleForm(forms.Form):
    
    lab = forms.CharField(widget=forms.RadioSelect())
    prof = forms.CharField(widget=forms.RadioSelect())
    time = forms.CharField(widget=forms.RadioSelect())
    section = forms.CharField(widget=forms.HiddenInput())
    course = forms.CharField(widget=forms.HiddenInput())
    
    