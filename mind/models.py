from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone



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
    description = models.TextField(("story_of_member"), null=True, blank=True)
    img = models.ImageField(("img_of_person"), null=True, blank=True)  # Specify upload_to

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'

class Newsletter(models.Model):
    title = models.CharField(("title"), max_length=100, null=True, blank=True, unique=True)
    img = models.ImageField(("img_of_newsletter"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    description = RichTextField(("description_of_newsletter"), null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

class Newsletterin(models.Model):
    img1 = models.ImageField("img_of_newsletter1", upload_to=None, null=True, blank=True)
    subtitle1 = RichTextField("description_of_newsletter1", null=True, blank=True,)
    related_newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    title = models.CharField(("title"), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'newsletterin'
        verbose_name_plural = 'newsletterins'



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Article(models.Model):
    title_article = RichTextField(("title_article"), null=True, blank=True)
    subtitle = RichTextField(("subtitle for card article"), null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(("prsoto def str ga"), max_length=100, null=True, blank=True)
    published_date = models.DateTimeField("Published Date", default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='Article')
    img = models.ImageField("long image", upload_to=None, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or "No title"
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-published_date']

class Articlein(models.Model):
    title_article = models.CharField(("title article"), max_length=200, null=True, blank=True)
    subtitle = models.TextField(("subtitle article"),  null=True, blank=True)
    img = models.ImageField("long image", upload_to=None, null=True, blank=True)
    title_first_article = models.CharField(("title_first_article"), max_length=200, null=True, blank=True)
    content1 = RichTextField("content for frist p", null=True, blank=True,)
    img1 = models.ImageField("img of in left ", upload_to=None, null=True, blank=True)
    content2 = RichTextField("content for second p", null=True, blank=True,)
    img2 = models.ImageField("img of in left under ", upload_to=None, null=True, blank=True)
    content3 = RichTextField("content for last before go right", null=True, blank=True,)
    content4 = RichTextField("righ column continue left", null=True, blank=True,)
    title_second_article = models.CharField(("title_second_article"), max_length=200, null=True, blank=True)
    content5 = RichTextField("content for right", null=True, blank=True,)
    img3 = models.ImageField("img for right  ", upload_to=None, null=True, blank=True)
    content6 = RichTextField("content for right", null=True, blank=True,)
    related_article = models.OneToOneField(Article, on_delete=models.CASCADE, unique=True, blank=True, null=True,)
    title = models.CharField(("title"), max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.title or "No title"

    class Meta:
        verbose_name = 'articlein'
        verbose_name_plural = 'articleins'



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

