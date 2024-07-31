from django.contrib import admin
from .models import Newsletter, Article, Work, Team

# Register your models here.
admin.site.register(Team)
admin.site.register(Work)
admin.site.register(Newsletter)
admin.site.register(Article)
from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    subtitle = forms.CharField(widget=CKEditorWidget())
