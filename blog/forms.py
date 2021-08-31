from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog, Keyword, Reply


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {
            'keywords': 'Keywords',
            'title': 'Title',
            'body': 'Body of Text',
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
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ['blog', 'user_profile']
        labels = {
            'body': 'Your Comment',
        }