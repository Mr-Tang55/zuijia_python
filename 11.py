# import os
# import sys
#
#
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zuijia.settings")
#     import django
#     django.setup()
#     from apps.Goods.models import *
#     t =[]
#     for f in range(106879,1000062):
#         g =Goods.objects.filter(id=f).values("goods_category__price")
#         for h in g:
#            t.append(h.get('goods_category__price'))
#         o = min(t)
#         Goods.objects.filter(id=f).update(price=o)
#         t = []
# s = {1:3}
# g = {5:6}
# h = {5:6}
# a = {s,g,h}
# print(a)

a ="style.name"
print(a.split("."))