import os
import sys
import random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zuijia.settings")
    import django
    django.setup()
    from apps.Goods.models import *

    i =Goods.objects.get(id=1)
    Goods_category.objects.create(goods=i, price=2,
                                  images='goods/images/Goods_images/2019/03/4.jpg',
                                  size='10*18mm', color="测试" + str(999 + 1),
                                  goods_sn=str(random.randint(1, 3000)), inventory=random.randint(1, 9999),
                                  purchase_quantity=random.randint(1, 3000), )
