from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'apps.Goods'

    def ready(self):
        import apps.Goods.signals
