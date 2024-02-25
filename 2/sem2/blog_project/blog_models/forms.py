import pdb

from django import forms
from . import models


class Author_form(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'surname', 'email', 'bio', 'birth_date']
        exclude = ['full_name', 'pk']


class Article_form(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title',
                  'content',
                  'publication_date',
                  'tags',
                  'isPublished', 'author', ]
        exclude = ['views']
