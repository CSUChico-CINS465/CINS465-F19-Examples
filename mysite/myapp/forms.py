from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models


class SuggestionForm(forms.Form):
    suggestion = forms.CharField(label='Suggestion', max_length=240, validators=[validate_slug])

class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=240, validators=[validate_slug])

    def save(self, request, sugg_id, commit=True):
        sugg_instance = models.Suggestion.objects.get(id=sugg_id)
        new_comm = models.Comment(
            suggestion=sugg_instance,
            comment=self.cleaned_data["comment"])
        new_comm.author = request.user
        if commit:
            new_comm.save()
        return new_comm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
