from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

class pollmeConfig(AppConfig):
    name = 'pollme'

    def ready(self):
        import pollme.signals
