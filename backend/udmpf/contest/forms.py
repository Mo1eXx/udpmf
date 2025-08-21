from django import forms

from phonebook.models import Kontakt


class ContestForm(forms.ModelForm):

    class Meta:
        model = Kontakt
        exclude = ('created_at', 'output_order')
