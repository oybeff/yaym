from django.apps import AppConfig


class MindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mind'

from django.apps import AppConfig

class MindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mind'

    def ready(self):
        import mind.signals  # This ensures the signals are registered
