from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('Blogger', 'title', 'image', 'video', 'category', 'description')
        widgets = {
            'Blogger': forms.TextInput(attrs={'placeholder': 'blogger name',
                                              'class': 'form-control mb-4'
                                              }),
            'title': forms.TextInput(attrs={'placeholder': ' Title',
                                            'class': 'form-control mb-4'
                                            }),
            'description': forms.Textarea(attrs={'placeholder': 'Blog description',
                                                 'class': 'form-control mb-4'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name',
                                           'class': 'email input-standard-grey'
                                           }),
            'body':forms.Textarea(attrs={'placeholder':'Your Comment',
                                         'class':'input-text input-standard-grey'})

        }
