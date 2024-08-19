from django.contrib import admin
from .models import Newsletter, Article, Work, Team, Newsletterin, Articlein

# Register your models here.
admin.site.register(Team)
admin.site.register(Work)
admin.site.register(Newsletterin)
admin.site.register(Newsletter)
admin.site.register(Article)
admin.site.register(Articlein)
from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    subtitle = forms.CharField(widget=CKEditorWidget())



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'published_date', 'category')
    search_fields = ('title1', 'title_article', 'subtitle')
    list_filter = ('category',)

from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
