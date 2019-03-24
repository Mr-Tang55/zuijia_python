from django.db.models.signals import post_save
from apps.Goods.models import *

def my_callback(instance,*args, **kwargs):
    """
    dajngo的信号机制
    :param instance: 写入数据库的数据
    :param args:
    :param kwargs:  所有的数据结构，包括created等于Ture就代表数据已经改过
    :return:
    """
    if kwargs.get('created'):
        id = instance.goods_id
        price = Goods_category.objects.filter(goods_id=id).values('price')
        price_list = []
        for i in price:
            price_list.append(i.get('price'))
        print(price_list)

        min_price = min(price_list)
        print(min_price)
        Goods.objects.filter(id=id).update(price=min_price)





post_save.connect(my_callback,sender=Goods_category,)