from django import forms
from django.core.validators import validate_slug

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(label='Suggestion', max_length=240,validators=[validate_slug])