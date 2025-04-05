from django import forms
from django.http import HttpResponse
from ..models import CustomerBotFlow


class SampleForm(forms.Form):
    name = forms.CharField(label='Your name')
    # name = CustomerBotFlow.objects.get(id=1).id