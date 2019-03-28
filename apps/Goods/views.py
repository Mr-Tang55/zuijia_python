import logging
from django.db.models import F
from rest_framework import mixins
from rest_framework.mixins import *
from rest_framework import filters      #搜索模块
from django.db.models.query import QuerySet
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend #过滤模块
from rest_framework_extensions.cache.mixins import CacheResponseMixin


from .models import *
from .filter import *
from .serializer import *
from units.filter import Goods_Filters
from units.Pagination import Goods_Pagination




# # 生成一个以当前文件名为名字的logger实例
# logger = logging.getLogger(__name__)
# # 生成一个名为collect的logger实例
# collect_logger = logging.getLogger("collect")


class Index(CacheResponseMixin,ViewSetMixin,APIView):
    def list(self, request, *args, **kwargs):
        ret={"code":100,"data":None}
        try:
            #轮播图
            carousel = IndexImg.objects.all().order_by('ord')
            carousel_serializers = IndexImg_Serializers(instance=carousel,many=True, context={"request":request})
            carousel = {'carousel':carousel_serializers.data}

            #专栏
            special = Special.objects.all().order_by('-add_time')[:3]
            special_serializers = Special_Serializers(instance=special,many=True, context={"request":request})
            special = {'special':special_serializers.data}

            #心水特色大图
            idenx_shuixin_large = Idenx_shuixin_Large.objects.all().order_by('-add_time')[:2]
            idenx_shuixin_large_serializers = Idenx_shuixin_Large_Serializers(instance=idenx_shuixin_large,
                                                                              many=True, context={"request":request})
            idenx_shuixin_large = {'idenx_shuixin_large':idenx_shuixin_large_serializers.data}

            #心水特色小图
            idenx_shuixin_little = Idenx_shuixin_little.objects.all()[:4]
            idenx_shuixin_little_serializers =Idenx_shuixin_little_Serializers(instance=idenx_shuixin_little,
                                                                               many=True, context={"request":request})
            idenx_shuixin_little = {'idenx_shuixin_little':idenx_shuixin_little_serializers.data}

            # 摆件花艺
            idenx_baijiahuayi_little = Idenx_baijiahuayi_little.objects.all().order_by('-add_time')[:6]
            idenx_baijiahuayi_little_serializers = Idenx_baijiahuayi_little_Serializers(
                instance=idenx_baijiahuayi_little,many=True, context={"request":request})
            idenx_baijiahuayi_little = {'idenx_baijiahuayi_little': idenx_baijiahuayi_little_serializers.data}

            #壁画北欧
            idenx_bihuabeio_little = Idenx_bihuabeio_little.objects.all()[:12]
            idenx_bihuabeio_little_serializers = Idenx_bihuabeio_little_Serializers(instance=idenx_bihuabeio_little,many=True, context={"request":request})
            idenx_bihuabeio_little = {"idenx_bihuabeio_little":idenx_bihuabeio_little_serializers.data}

            ret = {"code": 100, "data": [special,
                                         idenx_shuixin_large,idenx_shuixin_little,
                                         idenx_baijiahuayi_little,idenx_bihuabeio_little]}
            return Response(ret)
        except Exception as e:
            ret = {'code':101,'error':'数据获取失败'}
            return Response(ret)


class Style(CacheResponseMixin,ViewSetMixin,APIView):
    # 商品所属装饰风格,将其单独设置一个API，方便进入二级页面时前端显示商品类别
    def list(self, request, *args, **kwargs):
        ret={"code":100,"data":None}
        try:
            goodsstyle = GoodsStyle.objects.filter(is_index=True)
            goodsstyle_serializers = GoodsStyle_Serializers(instance=goodsstyle, many=True,
                                                            context={"request": request})
            ret = {"code": 100, "data":goodsstyle_serializers.data}
            return Response(ret)
        except Exception as e:
            ret = {'code': 101, 'error': '数据获取失败'}
            return Response(ret)


class Style_goods(GenericViewSet,mixins.ListModelMixin):
    # 装饰风格商品展示数据
    queryset = Goods.objects.all()
    serializer_class = Goods_Serializers
    pagination_class = Goods_Pagination

    def list(self, request, *args, **kwargs):
        ret = {"code": 100, "data": None}
        try:
            pk = kwargs.get('pk')
            queryset = Goods.objects.filter(style=pk, status=1)
            if queryset.count() == 0:
                ret = {"code": 102, 'error': '没有展示数据'}
                return Response(ret)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True,context={"request":request})
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            ret = {'code': 101, 'error': '数据获取失败'}
            return Response(ret)


class Category(CacheResponseMixin,ViewSetMixin,APIView):
    # 商品所属类别,将其单独设置一个API，方便进入二级页面时前端显示商品类别
    def list(self, request, *args, **kwargs):
        ret={"code":100,"data":None}
        try:
            goodscategory = GoodsCategory.objects.all()
            goodscategory_serializers = Goodcategory_Serializers(instance=goodscategory, many=True,
                                                                 context={"request": request})

            ret = {"code": 100, "data":goodscategory_serializers.data}
            return Response(ret)

        except Exception as e:
            ret = {'code': 101, 'error': '数据获取失败'}
            return Response(ret)


#装饰摆件,布艺软饰二级页面及所属的三级页面
class Two_zhuanshibianjian(GenericViewSet,ListModelMixin):
    queryset = Goods.objects.filter()
    serializer_class = Goods_Serializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = Goods_Filters

    def list(self, request, *args, **kwargs):
        ret = {"code": 100, "data": None}
        try:
            pk = self.kwargs.get('pk')

            top_img = None
            if int(pk) in [3,4,5]:
                #装饰摆件顶部推荐大图
                top_img = Two_zhuanshibianjian_Large.objects.all().order_by("-add_time")[:1]
            elif int(pk) in [4,6,7]:
                # 布艺软饰顶部推荐大图
                top_img = Two_bupiruanshi_Large.objects.all().order_by("-add_time")[:1]
            else:
                ret = {"code": 103, 'error': '参数不正确'}
                return Response(ret)
            img_serializers = Idenx_shuixin_little_Serializers(instance=top_img, many=True, context={"request": request})
            goodsstyle = {"goodsstyle_serializers": img_serializers.data}

            #页面显示的商品
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            below_goods = {'below_goods':serializer.data}
            ret = {"code": 100, "data": [goodsstyle,below_goods]}
            return Response(ret)
        except Exception as e:
            ret = {'code': 101, 'error': '数据获取失败'}
            return Response(ret)

    def get_queryset(self):
        #将queryset的数据进行过滤
        pk = self.kwargs.get('pk')
        queryset = self.queryset.filter(category=pk,status=1)[:16]
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset


# # 首页商品轮播大图
# class RecommendGoods_Views(GenericViewSet,ListModelMixin):
#     queryset = IndexImg.objects.all().order_by('ord')
#     serializer_class = IndexImg_Serializers
#
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