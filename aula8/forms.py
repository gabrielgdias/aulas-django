from aula8.models import Pet
from django import forms

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'

    def clean_nome(self):
        pet_name = self.cleaned_data.get('nome')
        if pet_name == 'Putinho':
            raise forms.ValidationError("Nome muito feio")
        return self.cleaned_data
