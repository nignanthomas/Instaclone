from django import forms
from .models import Post,Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['upload_by', 'pub_date','likes']


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
