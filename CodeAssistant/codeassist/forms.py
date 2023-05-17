from django.forms import ModelForm
from django import forms


class AssistChat(forms.Form):
    userInput  = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': ' Enter your text here'}))
    output = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder': ' Output'}))
    # add submit button
    # submit = forms.CharField(required=False, widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Submit'}))