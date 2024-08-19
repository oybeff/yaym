from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article, Articlein

@receiver(post_save, sender=Article)
def create_related_articles(sender, instance, created, **kwargs):
    if created:
        # Example logic to automatically add related articles
        # This can be based on any criteria, e.g., category, tags, etc.
        related_articles = Article.objects.filter(category=instance.category).exclude(id=instance.id)[:5]
        for related_article in related_articles:
            Articlein.objects.create(
                title_article=related_article.title1,
                subtitle=related_article.subtitle,
                related_article=instance
            )
