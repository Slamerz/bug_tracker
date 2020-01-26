from django import forms
from BugsBugsBugs.models import Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description'
        ]
