from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        """Override this to put in:
            User system checks
            User signal registration
        """
        try:
            from .signals import user_signed_up  # noqa F401
        except ImportError:
            pass
