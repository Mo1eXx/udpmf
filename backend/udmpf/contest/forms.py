from django import forms

from phonebook.models import Kontakt


class ContestForm(forms.ModelForm):

    class Meta:
        model = Kontakt
        fields = '__all__'
