from django.apps import AppConfig

class SignalDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_demo'

    def ready(self):
        import signal_demo.signals  # Import your signals
