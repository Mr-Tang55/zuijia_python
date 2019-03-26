import logging
from django.shortcuts import render
from django.db.models import F
from rest_framework.viewsets import ViewSetMixin
from django.db.models.query import QuerySet
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.mixins import *
from django_filters.rest_framework import DjangoFilterBackend #过滤模块
from rest_framework import filters  #搜索模块
# Create your views here.
from .models import *
from .serializer import *
from .filter import *
# from units.drf_authentication import Auth
from rest_framework_extensions.cache.mixins import CacheResponseMixin


from units.Pagination import Goods_Pagination



# # 生成一个以当前文件名为名字的logger实例
# logger = logging.getLogger(__name__)
# # 生成一个名为collect的logger实例
# collect_logger = logging.getLogger("collect")


class Index(CacheResponseMixin,ViewSetMixin,APIView):
    def list(self, request, *args, **kwargs):
        ret={"code":100,"data":None}
        try:
            goodsstyle = GoodsStyle.objects.filter(is_index=True)
            goodsstyle_serializers = GoodsStyle_Serializers(instance=goodsstyle,many=True,context={"request":request})
            goodsstyle = {"goodsstyle_serializers":goodsstyle_serializers.data}

            goodscategory = GoodsCategory.objects.all()
            goodscategory_serializers = Goodcategory_Serializers(instance=goodscategory,many=True, context={"request":request})
            goodscategory = {'goodscategory':goodscategory_serializers.data}

            carousel = IndexImg.objects.all().order_by('ord')
            carousel_serializers = IndexImg_Serializers(instance=carousel,many=True, context={"request":request})
            carousel = {'carousel':carousel_serializers.data}
            #
            special = Special.objects.all().order_by('-add_time')[:3]
            special_serializers = Special_Serializers(instance=special,many=True, context={"request":request})
            special = {'special':special_serializers.data}
            #
            idenx_shuixin_large = Idenx_shuixin_Large.objects.all().order_by('-add_time')[:2]
            idenx_shuixin_large_serializers = Idenx_shuixin_Large_Serializers(instance=idenx_shuixin_large,
                                                                              many=True, context={"request":request})
            idenx_shuixin_large = {'idenx_shuixin_large':idenx_shuixin_large_serializers.data}
            #
            idenx_shuixin_little = Idenx_shuixin_little.objects.all()[:4]
            idenx_shuixin_little_serializers =Idenx_shuixin_little_Serializers(instance=idenx_shuixin_little,
                                                                               many=True, context={"request":request})
            idenx_shuixin_little = {'idenx_shuixin_little':idenx_shuixin_little_serializers.data}

            idenx_baijiahuayi_little = Idenx_baijiahuayi_little.objects.all().order_by('-add_time')[:6]
            idenx_baijiahuayi_little_serializers = Idenx_baijiahuayi_little_Serializers(
                instance=idenx_baijiahuayi_little,many=True, context={"request":request})
            idenx_baijiahuayi_little = {'idenx_baijiahuayi_little': idenx_baijiahuayi_little_serializers.data}

            idenx_bihuabeio_little = Idenx_bihuabeio_little.objects.all()[:12]
            idenx_bihuabeio_little_serializers = Idenx_bihuabeio_little_Serializers(instance=idenx_bihuabeio_little,many=True, context={"request":request})
            idenx_bihuabeio_little = {"idenx_bihuabeio_little":idenx_bihuabeio_little_serializers.data}

            ret = {"code": 100, "data": [goodsstyle,goodscategory,carousel,special,
                                         idenx_shuixin_large,idenx_shuixin_little,
                                         idenx_baijiahuayi_little,idenx_bihuabeio_little]}
            return Response(ret)
        except Exception as e:
            ret = {'code':101,'error':'数据获取失败'}
            return Response(ret)

class Style(GenericViewSet,mixins.ListModelMixin,):
    queryset = Goods.objects.all()
    serializer_class = Goods_Serializers
    pagination_class = Goods_Pagination

    def list(self, request, *args, **kwargs):
        ret = {"code": 100, "data": None}
        pk = kwargs.get('pk')
        queryset = Goods.objects.filter(category=pk, status=1)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        # try:
        #
        # except Exception as e:
        #     ret = {'code': 101, 'error': '数据获取失败'}
        #     return Response(ret)

    # def list(self, request, *args, **kwargs):
    #     ret = {"code": 100, "data": None}
    #     try:
    #         pk = kwargs.get('pk')
    #         # GOODS的style这里要不要做索引？数据量一大就可能会很慢
    #         goods = Goods.objects.filter(category=pk,status=1)
    #         page_obj = Goods_Pagination()
    #         page_article = page_obj.paginate_queryset(queryset=goods, request=request, view=self)
    #         goods__serializers = Goods_Serializers(instance= page_article,many=True)
    #
    #         ret = {'code': 100, "data": goods__serializers.data}
    #     except Exception as e:
    #         ret = {'code': 101, 'error': '数据获取失败'}
    #         return Response(ret)
    #     return Response(ret)

# 首页商品轮播大图
# class RecommendGoods_Views(GenericViewSet,ListModelMixin):
#     queryset = IndexImg.objects.all().order_by('ord')
#     serializer_class = IndexImg_Serializers
#
#     def list(self, request, *args, **kwargs):
#         ret = {'code':100,'data':None}
#         try:
#             queryset = self.filter_queryset(self.get_queryset())
#             page = self.paginate_queryset(queryset)
#             if page is not None:
#                 serializer = self.get_serializer(page, many=True)
#                 return self.get_paginated_response(serializer.data)
#             serializer = self.get_serializer(queryset, many=True)
#             ret['data']=serializer.data
#             return Response(ret)
#         except Exception as e:
#             ret = {'code':101,'error':'数据获取失败'}
#             return Response(ret)