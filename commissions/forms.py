from django import forms
from .widgets import CustomClearableFileInput
from .models import Commissions


class CommissionsForm(forms.ModelForm):
    class Meta:
        model = Commissions
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name',
            'message': 'Extra comments',
            'email': 'Email address',
            'pet_num': 'Numbet of pets'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                if field != 'size' and field != 'pet_num' and field != 'media':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                    # add class for styling
                    self.fields[field].widget.attrs['class'] = 'profile-form-input'
                self.fields[field].label = False