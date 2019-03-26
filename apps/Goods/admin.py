from django.contrib import admin
import xadmin
from .models import *

# Register your models here.

xadmin.site.register(GoodsCategory)
xadmin.site.register(GoodsStyle)
xadmin.site.register(Goods)
xadmin.site.register(Goods_subdivide)
xadmin.site.register(Goods_category)
xadmin.site.register(GoodsImages)
xadmin.site.register(Special)
xadmin.site.register(SpecialGoods)
xadmin.site.register(Idenx_shuixin_Large)

xadmin.site.register(Spec_param)
xadmin.site.register(Spec_param_value)
xadmin.site.register( Spec_param_value_To_Goods_category)