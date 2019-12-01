from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user_name','title', 'text','year_in_school')
        labels = {
        "user_name": "Enter your name or the name of your Student Organization",
        "year_in_school": "What year of school are you?"
    }
