from .models import Post
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title','text')

        widgets = {
        'author':forms.TextInput(),
        'title':forms.TextInput(),
        'text':forms.Textarea()
        }
