from django.apps import AppConfig
from django.core.signals import request_finished


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    # def ready(self):
    #     from user import signals
    #     request_finished.connect(signals.user_is_created)

