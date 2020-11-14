from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import users.signals
