from rest_framework import serializers
from .models import *


class GoodsStyle_Serializers(serializers.ModelSerializer):
    """商品所属装饰风格,
    需要id来返回后端判断具体是哪个商品装饰风格
    name：显示商品装饰风格标题，
    images：首页装饰风格图片
    """
    class Meta:
        model=GoodsStyle
        fields = ('id', 'name', 'images')



class Goodcategory2_Serializers(serializers.ModelSerializer):
    """
    将Goodcategory2_Serializers的数据嵌套到Goodcategory_Serializers中
    """
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name', 'category_type')




class Goodcategory_Serializers(serializers.ModelSerializer):
    """
    用于序列化所有的商品目录
    id：商品目录的id，用于返回给后端来判断用户进入了哪个子商品页面
    name：商品目录的名字,给用户看的
    category_type：类目的级别，给前端判断，如果是第一级别会显示在首页的导航栏中
    sub_cat：被嵌套的第二级别的目录
    """
    sub_cat = Goodcategory2_Serializers(many=True)
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name', 'category_type','sub_cat')




    # 首页商品推荐大图
class IndexImg_Serializers(serializers.ModelSerializer):
    """
    首页轮播图的数据，
    id：轮播图id，有无无所谓
    goods：用于显示外键商品的id，好确定是进入哪个商品的详情页
    images：展示的图片
    ord：用于轮播图的排序
    """
    class Meta:
        model = IndexImg
        fields =("id","goods","images","ord")


#专栏数据
class Special_Serializers(serializers.ModelSerializer):
    """
    专栏数据
    id：专栏的id，用于返回给后端来判断用户进入了哪个专栏页面
    title: 专栏的名字，给用户展示用
    images：代表专栏的图片，展示用
    """
    class Meta:
        model =Special
        fields = ("id","title","images")


class Idenx_shuixin_Large_Serializers(serializers.ModelSerializer):
    """
    首页水心特色段的两张推荐大图
    id：水心特色段图片id，有无无所谓
    goods：用于显示外键商品的id，好确定是进入哪个商品的详情页
    images：展示的图片
    ord：用于轮播图的排序
    """
    class Meta:
        model =Idenx_shuixin_Large
        fields = ("id","goods","images","ord")

class Idenx_shuixin_little_Serializers(serializers.ModelSerializer):
    """
       首页水心特色段的推荐小图, 装饰摆件,布艺软饰顶部推荐图序列化
       id：水心特色段图片id，有无无所谓
       goods：用于显示外键商品的id，好确定是进入哪个商品的详情页
       images：展示的图片
       """
    class Meta:
        model =Idenx_shuixin_little
        fields = ("id","goods","images")


class Idenx_baijiahuayi_little_Serializers(serializers.Serializer):
    """
    首页摆件花艺段的推荐图片
    id：摆件花艺段图片id，有无无所谓
    F_id：用于显示外键商品的id，好确定是进入哪个商品的详情页
    images：展示的图片
    good:推荐商品的名字
    price：推荐商品的价格
    """
    id = serializers.IntegerField()
    F_id = serializers.CharField(source='goods.id')
    images = serializers.ImageField()
    good = serializers.CharField(source="goods.name")
    price = serializers.CharField(source="goods.price")

class Idenx_bihuabeio_little_Serializers(serializers.Serializer):
    """
    首页壁画北欧段的推荐图片
    id：壁画北欧段图片id，有无无所谓
    F_id：用于显示外键商品的id，好确定是进入哪个商品的详情页
    images：展示的图片
    good:推荐商品的名字
    price：推荐商品的价格
    """
    id = serializers.IntegerField()
    F_id = serializers.CharField(source="goods.id")
    images = serializers.ImageField()
    good = serializers.CharField(source="goods.name")
    price = serializers.CharField(source="goods.price")

class img_Serializers(serializers.ModelSerializer):
    """
    Goods_Serializers序列化器中添加了一个未在Goods表中的字段，
    此序列化器用于序列化那个不存在的字段，不序列化是不能转换成json格式的
    """
    class Meta:
        model=GoodsImages
        fields = ("images",)

# class Goods_Serializers(serializers.Serializer):
#     test=serializers.CharField(source="style.name")


class Goods_Serializers(serializers.ModelSerializer):
    """
    商品装饰风格的所有商品的序列化
    id:商品的id，返回给后端判断是哪个商品，好确定是进入哪个商品的详情页
    name:商品的名字，前端页面展示用
    category：商品所属类别的id,有无无所谓
    style：商品所属装饰风格的id,有无无所谓
    img：商品的展示图片
    price：商品价格
    sale：商品的销售额
    ship_free：给前端判断此商品是否包邮
    """
    img =serializers.SerializerMethodField()
    class Meta:
        model=Goods
        fields = ("id", "name", "category",'style','img','price','sale','ship_free')

    def get_img(self, obj):
        #添加一个未在Goods表中的字段，并且序列化
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