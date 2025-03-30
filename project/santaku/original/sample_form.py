from django import forms


class SampleForm(forms.Form):
    name = forms.CharField(label='Your name')