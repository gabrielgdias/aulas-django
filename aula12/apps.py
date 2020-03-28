from django.apps import AppConfig


class Aula12Config(AppConfig):
    name = 'aula12'

    def ready(self):
        import aula12.signals