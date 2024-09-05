from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'user_profile'
    def ready(self):
        import user_profile.signals