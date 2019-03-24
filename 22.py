# import random
#
# print(random.randint(1,2))
#
# print (random.sample('zyxwvutsrqponmlkjihgfedcba',5))


import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zuijia.settings")
    import django
    django.setup()
    from apps.Goods.models import *
    import random
    s = 725986
    for i in range(274014):
        y = GoodsCategory.objects.get(id=random.randint(1, 9))
        s = s + 1
        t = Goods.objects.create(name=str(s + 1) + '号测试商品', category=y, sale=random.randint(1, 5),
                                 synopsis=str(s + 1) + '号测试商品简介', content=str(s + 1) + '号测试商品详细',
                                 )
        for e in range(3):
            Goods_category.objects.create(goods=t, price=random.randint(1, 3000),
                                          images='goods/images/Goods_images/2019/03/4.jpg',
                                          size='10*18mm', color="测试" + str(s + 1),
                                          goods_sn=str(random.randint(1, 3000)), inventory=random.randint(1, 9999),
                                          purchase_quantity=random.randint(1, 3000), )
        for u in range(2):
            GoodsImages.objects.create(goods=t, images='goods/images/Goods_images/2019/03/4.jpg')
        print(s)
