from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Work(models.Model):
    subtitle = RichTextField(("description_of_newsletter"), null=True, blank=True)

    def __str__(self) -> str:
        return self.subtitle
    
    class Meta:
        verbose_name = "work"
        verbose_name_plural = "works"


class Team(models.Model):
    title = models.CharField(("full name"), max_length=100, null=True, blank=True)
    subtitle = models.CharField(("position_work"), max_length=250, null=True, blank=True)
    img = models.ImageField(("img_of_person"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'

class Newsletter(models.Model):
    title = models.CharField(("title"), max_length=100, null=True, blank=True)
    subtitle = RichTextField(("description_of_newsletter"), null=True, blank=True)
    img = models.ImageField(("img_of_newsletter"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    desciption = models.TextField(("description_of_newsletter"), null=True, blank=True)
    img = models.ImageField(("img_of_newsletter"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

class Article(models.Model):
    title = models.CharField(("title_of_article"), max_length=100, null=True, blank=True)
    subtitle = models.CharField(("name_of_article"), max_length=250, null=True, blank=True)
    title2 = models.CharField(("title_of_article"), max_length=100, null=True, blank=True)
    desciption = models.TextField(("description_of_article"), null=True, blank=True)
    img = models.ImageField(("img_of_article"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

# models.py
from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Ensure this is a DateField
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    
    def get_element_response(self):
        year = self.dob.year
        if 1950 <= year <= 1960:
            return "Response for 1950-1960"
        elif 1961 <= year <= 1971:
            return "Response for 1961-1971"
        elif 1972 <= year <= 1982:
            return "Response for 1972-1982"
        elif 1983 <= year <= 1994:
            return "Response for 1983-1994"
        elif 2005 <= year <= 2015:
            return "Response for 2005-2015"
        elif 2016 <= year <= 2026:
            return "Response for 2016-2026"
        else:
            return "General Response"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

