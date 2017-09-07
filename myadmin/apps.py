from django.apps import AppConfig


class MyadminConfig(AppConfig):
    name = 'myadmin'

    def ready(self):
        super(MyadminConfig,self).ready()
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('ma')
