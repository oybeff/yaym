from django.core.management.base import BaseCommand
from mind.models import Newsletterin  # YourModel ni to'g'ri modelingiz bilan almashtiring
from django.db.models import Count

class Command(BaseCommand):
    help = 'Duplicate slugsni yangilaydi'

    def handle(self, *args, **kwargs):
        duplicates = Newsletterin.objects.values('slug').annotate(slug_count=Count('slug')).filter(slug_count__gt=1)
        for duplicate in duplicates:
            new_slug = self.generate_unique_slug(duplicate)
            Newsletterin.objects.filter(slug=duplicate['slug']).update(slug=new_slug)
        self.stdout.write(self.style.SUCCESS('Slugs updated successfully'))

    def generate_unique_slug(self, duplicate):
        # Bu yerda o'ziga xos slug yaratish kodini qo'shing
        return f"{duplicate['slug']}-{duplicate['slug_count']}"
