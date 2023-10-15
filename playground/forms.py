from django import forms


class CreateScheduleForm(forms.Form):
    course = forms.CharField(max_length=255)
