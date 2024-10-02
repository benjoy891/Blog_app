from django import forms
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Write your post content here...'
        })
    )

    class Meta:
        model = PostModel
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Post Title'
            }),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Post Title'
            }),
            'content': forms.Textarea(attrs={
                'rows': 4,
                'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Edit your post content here...'
            }),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded-md p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Add comment here....'
        })
    )

    class Meta:
        model = Comment
        fields = ('content',)
