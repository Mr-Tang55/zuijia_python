from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


# 所属类别分类
class GoodsCategory(models.Model):
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
        (4, "四级类目"),
    )

    name = models.CharField(default="",max_length=30,verbose_name="分类名字",help_text="按类别分类")
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别",help_text="类目级别")
    parent_category = models.ForeignKey("self",null=True,blank=True,verbose_name="父类目级别",help_text="父目录",related_name="sub_cat")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品所属类别分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# # 所属风格分类
class GoodsStyle(models.Model):
    name = models.CharField(max_length=24,verbose_name="所属装饰风格",help_text="所属装饰风格")
    images = models.ImageField(verbose_name='商品图片', upload_to='goods/images/GoodsStyle/%Y/%m', null=True,blank=True) #不能为空
    is_index = models.BooleanField(verbose_name='是否在首页显示')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = "所属装饰风格"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# #商品参数组
# class Spec_group(models.Model):
#     cid = models.ForeignKey(GoodsCategory,verbose_name='商品分类id')
#     name = models.CharField(verbose_name='商品规格组',max_length=48)
#     class Meta:
#         verbose_name = "商品规格组"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.cid.name+"_"+self.name


#商品显示
class Goods(models.Model):
    CATEGORY_TYPE = (
        (1, "已发布"),
        (2, "未发布"),
        (3, "草稿"),
        (4, "下架"),
        (5, "已删除"),
    )
    name = models.CharField(max_length=64, verbose_name='商品名称')
    category = models.ForeignKey(GoodsCategory, verbose_name='所属类别', related_name='Goods_and_GoodsCategory')
    style = models.ForeignKey(GoodsStyle, verbose_name="所属装饰风格", related_name="goodsstyle", null=True,
                              blank=True)
    price = models.FloatField(verbose_name='价格',null=True, blank=True, help_text='不需要填写，由程序自动计算',)
    sale = models.IntegerField(verbose_name='销售额', default=0)
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    status = models.IntegerField(verbose_name='商品所属状态',choices=CATEGORY_TYPE)
    

    class Meta:
        verbose_name = "商品分表一"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 商品详情主图片
class GoodsImages(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='商品名',related_name='GoodsImages_and_Goods')
    images = models.ImageField(verbose_name='商品图片',upload_to='goods/images/Goods_images/%Y/%m',null=True,blank=True)
    is_imagesis = models.BooleanField(default=False, verbose_name='是否为商品主图')
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name+'_图片'

#商品详情
class Goods_subdivide(models.Model):
    goods_subdivide = models.OneToOneField(Goods, verbose_name='商品细分字段', help_text='减小表读取压力，将商品表进行分表')
    synopsis = models.CharField(max_length=256, verbose_name='商品简介', blank=True, null=True)
    content = RichTextUploadingField(verbose_name='商品详情')
    hits = models.IntegerField(verbose_name='点击数', default=0)
    goods_environmental = models.TextField(verbose_name='环保信息', null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    si_new = models.BooleanField(default=False, verbose_name="是否为新品")
    spu = models.CharField(max_length=48,verbose_name="商品的spu码")


    class Meta:
        verbose_name = "商品分表二"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_subdivide.name

# 商品规格
class Goods_category(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='所属商品',related_name='goods_category')
    price = models.FloatField(verbose_name='价格')
    goods_sn = models.CharField(max_length=256,default="",verbose_name="商品sku")
    inventory = models.IntegerField(verbose_name='库存数', default=0)
    purchase_quantity = models.IntegerField(verbose_name='销售额',default=0)
    order = models.IntegerField(verbose_name='商品显示顺序', default=1,help_text='1为最大，越大越靠前显示') #这里需要创建唯一约束
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品规格"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

#商品规格key表
class Spec_param(models.Model):
    cid = models.ForeignKey(GoodsCategory, verbose_name='商品所属分类id')
    name = models.CharField(max_length=255,verbose_name='参数名')
    is_key = models.BooleanField(verbose_name="是否为关键属性", help_text="为True会此属性出现在商品详情页规格栏中")
    sort = models.IntegerField(verbose_name="排序，越小权重越高")
    searching = models.BooleanField(verbose_name='是否用于搜索过滤')
    numeric = models.BooleanField(verbose_name="是否是数字类型参数，true或false")
    is_color = models.BooleanField(verbose_name="是否为颜色属性",help_text="为True时会出现商品颜色图片上传功能")
    unit = models.CharField(max_length=16, blank=True, null=True, verbose_name="数字类型参数的单位，非数字类型可以为空")
    generic = models.BooleanField(verbose_name='此属性是否是用于生产skuID，true或false')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品规格key表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cid.name + "_" + self.name

#商品规格value表
class Spec_param_value(models.Model):
    spec_param_id = models.ForeignKey(Spec_param,verbose_name='参数名')
    value = models.CharField(max_length=255,verbose_name='参数值')
    images = models.ImageField(verbose_name='商品图片', upload_to='goods/images/Spec_param_value/%Y/%m', null=True,
                               blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "商品规格value表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.spec_param_id.name + "_" + self.value


#商品参数与商品详情关联表，这样设置是为了保持商品参数与商品详情关联表灵活性，可以随意配置
class Spec_param_value_To_Goods_category (models.Model):
    spec_param_value_id = models.ForeignKey(Spec_param_value,verbose_name='关联的规格参数表')
    goods_category = models.ForeignKey(Goods_category,verbose_name='关联的所属商品表')

    class Meta:
        verbose_name = "商品参数与商品详情关联表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_category.goods.name+self.spec_param_value_id.value

#专栏名
class Special(models.Model):
    title = models.CharField(verbose_name='专栏名',max_length=24)
    images = models.ImageField(verbose_name='专栏图片', upload_to='goods/images/Special/%Y/%m', unique=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = "专栏名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

#专栏与商品
class SpecialGoods(models.Model):
    title = models.ForeignKey(Special,verbose_name='关联的专栏')
    goods= models.ForeignKey(Goods,verbose_name='关联的商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        verbose_name = "专栏与商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title.title+"_"+self.goods.name


#
# 商品图抽象基类
class Img(models.Model):
    goods = models.ForeignKey(Goods,verbose_name='所属具体商品',related_name="%(app_label)s_%(class)s_related")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True

    def __str__(self):
        return self.goods.name+".jpg"


#首页轮播图
class IndexImg(Img):
    CATEGORY_TYPE = ((1, "顺序1"),(2, "顺序2"),(3, "顺序3"),)
    images = models.ImageField(verbose_name='主打商品图片',upload_to='goods/images/IndexImg/%Y/%m',unique=True)
    ord = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='图片顺序，1为最前', unique=True)

    class Meta:
        verbose_name = "首页大图推荐商品图"
        verbose_name_plural = verbose_name


#水心特色栏目商品大图
class Idenx_shuixin_Large(Img):
    CATEGORY_TYPE = ((1, "顺序1"), (2, "顺序2"), )
    images = models.ImageField(verbose_name='首页_水心特色商品大图', upload_to='goods/images/Idenx_shuixin_Large/%Y/%m', unique=True)
    ord = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='图片顺序，1为最前', unique=True,blank=True,null=True)
    # 不能为null
    class Meta:
        verbose_name = "首页_水心特色商品大图"
        verbose_name_plural = verbose_name


#水心特色栏目商品小图
class Idenx_shuixin_little(Img):
    images = models.ImageField(verbose_name='首页_水心特色商品小图', upload_to='goods/images/Idenx_shuixin_little/%Y/%m', unique=True)

    class Meta:
        verbose_name = "首页_水心特色商品小图"
        verbose_name_plural = verbose_name


#首页_摆件-花艺栏目图片
class Idenx_baijiahuayi_little(Img):
    images = models.ImageField(verbose_name='首页_摆件-花艺首页商品图', upload_to='goods/images/Idenx_baijiahuayi_little/%Y/%m', unique=True)

    class Meta:
        verbose_name = "首页_摆件-花艺首页商品图"
        verbose_name_plural = verbose_name


#壁画-北欧栏目图片
class Idenx_bihuabeio_little(Img):
    images = models.ImageField(verbose_name='首页_壁画-北欧首页商品图', upload_to='goods/images/Idenx_bihuabeio_little/%Y/%m', unique=True)

    class Meta:
        verbose_name = "首页_壁画-北欧首页商品图"
        verbose_name_plural = verbose_name




# 二级-装饰摆件-顶部大图
class Two_zhuanshibianjian_Large(Img):
    images = models.ImageField(verbose_name='二级-装饰摆件-顶部大图', upload_to='goods/images/two_zhuanshibianjian_Large/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-装饰摆件-顶部大图"
        verbose_name_plural = verbose_name
    # 二级-装饰摆件-商品图

#二级-装饰摆件-商品小图
class Two_zhuanshibianjian_little(Img):
    images = models.ImageField(verbose_name='二级-装饰摆件-推荐大图', upload_to='goods/images/two_zhuanshibianjian_little/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-装饰摆件-推荐小图"
        verbose_name_plural = verbose_name





# 二级-布艺软饰-顶部大图
class Two_bupiruanshi_Large(Img):
    images = models.ImageField(verbose_name='二级-布艺软饰-顶部大图', upload_to='goods/images/two_bupiruanshi_Large/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-布艺软饰-顶部大图"
        verbose_name_plural = verbose_name
    # 二级-装饰摆件-商品图

#二级-布艺软饰-商品小图
class Two_bupiruanshi_little(Img):
    images = models.ImageField(verbose_name='二级-布艺软饰-商品小图', upload_to='goods/images/two_bupiruanshi_little/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-布艺软饰-商品小图"
        verbose_name_plural = verbose_name



# 二级-墙饰壁挂-顶部大图
class Two_qiangshibigua_Large(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-顶部大图', upload_to='goods/images/two_qiangshibigua_Large/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-墙饰壁挂-顶部大图"
        verbose_name_plural = verbose_name


# 二级-墙饰壁挂-简约现代大图
class Two_qiangshibigua_xiandai_Large(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-简约现代大图', upload_to='goods/images/two_qiangshibigua_xiandai_Large/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-墙饰壁挂-简约现代大图"
        verbose_name_plural = verbose_name
# 二级-墙饰壁挂-简约现代小图
class Two_qiangshibigua_xiandai_little(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-简约现代小图', upload_to='goods/images/two_qiangshibigua_xiandai_little/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-墙饰壁挂-简约现代小图"
        verbose_name_plural = verbose_name


# 二级-墙饰壁挂-浓情欧式大图
class Two_qiangshibigua_noqiangashi_Large(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-浓情欧式大图', upload_to='goods/images/two_qiangshibigua_noqiangashi_Large/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-浓情欧式大图"
        verbose_name_plural = verbose_name
# 二级-墙饰壁挂-浓情欧式小图
class Two_qiangshibigua_noqiangashi_little(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-浓情欧式小图', upload_to='goods/images/two_qiangshibigua_noqiangashi_little/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-浓情欧式小图"
        verbose_name_plural = verbose_name


# 二级-墙饰壁挂-雅致中式大图
class Two_qiangshibigua_zhiyazhongshi_Large(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-雅致中式大图', upload_to='goods/images/two_qiangshibigua_zhiyazhongshi_Large/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-雅致中式大图"
        verbose_name_plural = verbose_name
# 二级-墙饰壁挂-雅致中式小图
class Two_qiangshibigua_zhiyazhongshi_little(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-雅致中式小图', upload_to='goods/images/two_qiangshibigua_zhiyazhongshi_little/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-雅致中式小图"
        verbose_name_plural = verbose_name


# 二级-墙饰壁挂-浪漫美式大图
class Two_qiangshibigua_langmanmeishi_Large(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-雅致中式大图', upload_to='goods/images/two_qiangshibigua_langmanmeishi_Large/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-浪漫美式大图"
        verbose_name_plural = verbose_name
# 二级-墙饰壁挂-浪漫美式小图
class Two_qiangshibigua_langmanmeishi_little(Img):
    images = models.ImageField(verbose_name='二级-墙饰壁挂-雅致中式小图', upload_to='goods/images/two_qiangshibigua_langmanmeishi_little/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-墙饰壁挂-浪漫美式小图"
        verbose_name_plural = verbose_name



# 二级-蜡艺香薰-顶部大图
class Two_nayixiangxun_Large(Img):
    images = models.ImageField(verbose_name='二级-蜡艺香薰-顶部大图', upload_to='goods/images/two_nayixiangxun_Large/%Y/%m',unique=True)

    class Meta:
        verbose_name = "二级-蜡艺香薰-顶部大图"
        verbose_name_plural = verbose_name

# 二级-蜡艺香薰-香薰精油大图
class Two_qiangshibigua_xiangxunjingyou_Large(Img):
    images = models.ImageField(verbose_name='二级-蜡艺香薰-香薰精油大图', upload_to='goods/images/two_qiangshibigua_xiangxunjingyou_Large/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-蜡艺香薰-香薰精油大图"
        verbose_name_plural = verbose_name
# 二级-蜡艺香薰-香薰精油小图
class Two_qiangshibigua_xiangxunjingyou_little(Img):
    images = models.ImageField(verbose_name='二级-蜡艺香薰-香薰精油小图', upload_to='goods/images/two_qiangshibigua_xiangxunjingyou_little/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-蜡艺香薰-香薰精油小图"
        verbose_name_plural = verbose_name

# 二级-蜡艺香薰-香薰炉大图
class Two_qiangshibigua_xiangxunlu_Large(Img):
    images = models.ImageField(verbose_name='二级-蜡艺香薰-香薰炉大图', upload_to='goods/images/two_qiangshibigua_xiangxunlu_Large/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-蜡艺香薰-香薰炉大图"
        verbose_name_plural = verbose_name
# 二级-蜡艺香薰-香薰炉小图
class Two_qiangshibigua_xiangxunlu_little(Img):
    images = models.ImageField(verbose_name='二级-蜡艺香薰-香薰炉小图', upload_to='goods/images/two_qiangshibigua_xiangxunlu_little/%Y/%m',
                               unique=True)
    class Meta:
        verbose_name = "二级-蜡艺香薰-香薰炉小图"
        verbose_name_plural = verbose_name




# 二级-创意家具-顶部大图
class Two_chuangyijiaju_Large(Img):
    images = models.ImageField(verbose_name='二级-创意家具-顶部大图', upload_to='goods/images/two_chuangyijiaju_Large/%Y/%m',
                               unique=True)

    class Meta:
        verbose_name = "二级-创意家具-顶部大图"
        verbose_name_plural = verbose_name



# 二级-创意家具-创意家具小图
class Two_chuangyijiaju_chuangyijiaju_little(Img):
    images = models.ImageField(verbose_name='二级-创意家具-创意家具小图',
                               upload_to='goods/images/two_chuangyijiaju_chuangyijiaju_little/%Y/%m',
                               unique=True)

    class Meta:
        verbose_name = "二级-创意家具-创意家具小图"
        verbose_name_plural = verbose_name


# 二级-创意家具-时尚新颖大图
class Two_chuangyijiaju_shisahngxinying_Large(Img):
    images = models.ImageField(verbose_name='二级-创意家具-时尚新颖大图',
                               upload_to='goods/images/two_chuangyijiaju_shisahngxinying_Large/%Y/%m',
                               unique=True)

    class Meta:
        verbose_name = "二级-创意家具-时尚新颖大图"
        verbose_name_plural = verbose_name


# 二级-创意家具-时尚新颖小图
class Two_chuangyijiaju_shisahngxinying_little(Img):
    images = models.ImageField(verbose_name='二级-创意家具-时尚新颖小图',
                               upload_to='goods/images/two_chuangyijiaju_shisahngxinying_little/%Y/%m',
                               unique=True)

    class Meta:
        verbose_name = "二级-创意家具-时尚新颖小图"
        verbose_name_plural = verbose_name

# 二级-创意家具-创意生活小图
class Two_chuangyishenghuo_chuangyishenghuo_little(Img):
    images = models.ImageField(verbose_name='二级-创意家具-创意生活小图',
                               upload_to='goods/images/two_chuangyishenghuo_chuangyishenghuo_little/%Y/%m',
                               unique=True)

    class Meta:
        verbose_name = "二级-创意家具-创意生活小图"
        verbose_name_plural = verbose_name
