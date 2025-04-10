from django.apps import AppConfig


class ServerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .models import Status, Type

        def create_initial_data(sender, **kwargs):
            if not Status.objects.exists():
                Status.objects.create(name="Бизнес")
                Status.objects.create(name="Личное")
                Status.objects.create(name="Налог")
            if not Type.objects.exists():
                Type.objects.create(name="Пополнение")
                Type.objects.create(name="Списание")


        post_migrate.connect(create_initial_data, sender=self)
