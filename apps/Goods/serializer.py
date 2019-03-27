from rest_framework import serializers
from .models import *

class GoodsStyle_Serializers(serializers.ModelSerializer):
    class Meta:
        model=GoodsStyle
        fields = ('id', 'name', 'images')

# # 二级子商品目录
class Goodcategory2_Serializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name', 'category_type')

# 父级商品目录
class Goodcategory_Serializers(serializers.ModelSerializer):
    sub_cat = Goodcategory2_Serializers(many=True)
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name', 'category_type','sub_cat')
        #fields = "__all__"

    # 首页商品推荐大图
class IndexImg_Serializers(serializers.ModelSerializer):
    class Meta:
        model = IndexImg
        fields =("id","goods","images","ord")

class Special_Serializers(serializers.ModelSerializer):
    class Meta:
        model =Special
        fields = ("id","title","images")

class Idenx_shuixin_Large_Serializers(serializers.ModelSerializer):
    class Meta:
        model =Idenx_shuixin_Large
        fields = ("id","goods","images","ord")

class Idenx_shuixin_little_Serializers(serializers.ModelSerializer):
    class Meta:
        model =Idenx_shuixin_little
        fields = ("id","goods","images")


class Idenx_baijiahuayi_little_Serializers(serializers.Serializer):
    id = serializers.IntegerField()
    F_id = serializers.CharField(source='goods.id')
    images = serializers.ImageField()
    good = serializers.CharField(source="goods.name")
    price = serializers.CharField(source="goods.price")

class Idenx_bihuabeio_little_Serializers(serializers.Serializer):
    id = serializers.IntegerField()
    F_id = serializers.CharField(source="goods.id")
    images = serializers.ImageField()
    good = serializers.CharField(source="goods.name")
    price = serializers.CharField(source="goods.price")

class img_Serializers(serializers.ModelSerializer):
    class Meta:
        model=GoodsImages
        fields = ("images",)

# class Goods_Serializers(serializers.Serializer):
#     test=serializers.CharField(source="style.name")


class Goods_Serializers(serializers.ModelSerializer):
    img =serializers.SerializerMethodField()

    class Meta:
        model=Goods
        fields = ("id", "name", "category",'style','img','price','sale','ship_free')

    def get_img(self, obj):
        queryset = obj.id
        img_obj =GoodsImages.objects.filter(id=queryset,is_imagesis=True).first()
        if img_obj:
            img = img_Serializers(instance=img_obj,many=False,context={'request': self.context['request']})
            return img.data
        return None

#
# # 二级页面商品推荐大图
# class Recommend_Goods2_serializers(serializers.ModelSerializer):
#     class Meta:
#         model = Recommend_Goods2
#         fields = ('id', 'name', 'good', 'images', 'site')
#
# # 商品图片
# # class Goods_images_serializers(serializers.ModelSerializer):
# #     class Meta:
# #         model = Goods_images
# #         fields = ('id', 'images')
#
# # 详情页商品规格序列化
# class Goods_category_serializers(serializers.ModelSerializer):
#     class Meta:
#         model = Goods_category
#         fields = ('id','price','size','color','goods_sn','inventory','purchase_quantity','images','order')
# #images,price  'id','name'
#
# # 详情页商品序列化
# class Goods_serializers(serializers.ModelSerializer):
#     goods_category = Goods_category_serializers(many=True)
#     category = serializers.CharField(source='category.name')
#     class Meta:
#         model = Goods
#         fields = ('id','name','category','synopsis','sale','ship_free','goods_environmental','si_new','goods_category')
#
#
# # 商品规格
# class Goods_category_serializers1(serializers.ModelSerializer):
#     class Meta:
#         model = Goods_category
#         fields = ('id','images')
# # 商品
# class Goods_serializers1(serializers.ModelSerializer):
#     goods_category = Goods_category_serializers1(many=True)
#     category = serializers.CharField(source='category.name')
#     class Meta:
#         model = Goods
#         fields = ('id','name','category',"least_price","highest_price",'goods_category')