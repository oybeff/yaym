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


from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


from django.core.exceptions import ValidationError

def save(self, *args, **kwargs):
    if Articlein.objects.filter(related_article=self.related_article).exists():
        raise ValidationError("This article already has a related entry.")
    super().save(*args, **kwargs)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_article', 'published_date', 'category')
    search_fields = ('title_article', 'subtitle')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title_article',)}
    actions = ['create_articlein']

    def create_articlein(self, request, queryset):
        for article in queryset:
            if not Articlein.objects.filter(related_article=article).exists():
                Articlein.objects.create(related_article=article)
        self.message_user(request, "Articlein objects created successfully.")
    create_articlein.short_description = "Create Articlein for selected articles"

