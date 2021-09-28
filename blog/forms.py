from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog, Keyword, Reply


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']
        labels = {
            'keywords': 'Keywords',
            'title': 'Title',
            'body': 'Body',
            'teaser': 'Teaser',
        }
        widgets = {
            'keywords': forms.CheckboxSelectMultiple,
        }
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        keywords = Keyword.objects.all()
        friendly_names = [(k.id, k.get_friendly_name()) for k in keywords]
        # update form keywords field to friendly name
        self.fields['keywords'].choices = friendly_names


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ['blog', 'author']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'body': 'Your comment'
        }

        for field in self.fields:
            if field != 'author':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # add class for styling
            self.fields[field].label = False
