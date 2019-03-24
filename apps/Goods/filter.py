import django_filters
from django.db.models import Q
from .models import *

class Goods_Filters(django_filters.rest_framework.FilterSet):
    category = django_filters.Filter(method='category_filter', label="商品分类")
    goods_category_price1 = django_filters.NumberFilter(lookup_expr='gte', label="最低价格", field_name='least_price')
    goods_category__price2 = django_filters.NumberFilter(lookup_expr='lte', label="最高价格", field_name='highest_price')
    si_new = django_filters.BooleanFilter(lookup_expr='exact', label="全部新品展示", field_name='si_new')
    index_NewGoods = django_filters.Filter(method='Index_NewGoods', label="首页新品展示,请写入参数1")
    si_recommend = django_filters.BooleanFilter(lookup_expr='exact', label="推荐商品展示", field_name='si_recommend')

    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

        # return filter

    def Index_NewGoods(self, queryset, name, value):
        # queryset为视图层的queryset = Goods.objects.all()中数据
        # value为前端传递过来的参数
        # __parent获得当前匹配元素集合中每个元素的父元素
        # #默认接收所有字段，使用name参数后，只接收name参数的字段  {name: value}
        if value=='1':
            filter = queryset.filter(si_new=True)
            filter = filter[0:10]
            return filter
        return None


#首页新商品展示与全部新商品
    class RecommendGoods2__Filters(django_filters.rest_framework.FilterSet):
        si_new = django_filters.BooleanFilter(lookup_expr='exact', label="是否为新品", field_name='si_new')

# # 二级页面推荐商品大图过滤
# class RecommendGoods2__Filters(django_filters.rest_framework.FilterSet):
#     name = django_filters.CharFilter(help_text="输入所属房间id")
#
#     # class Meta:
#     #     modles = Goods
#     #     filter = ['name', ]


