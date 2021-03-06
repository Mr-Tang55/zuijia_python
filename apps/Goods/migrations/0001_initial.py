# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-24 18:26
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='商品名称')),
                ('price', models.FloatField(blank=True, help_text='不需要填写，由程序自动计算', null=True, verbose_name='价格')),
                ('sale', models.IntegerField(default=0, verbose_name='销售额')),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('status', models.IntegerField(choices=[(1, '已发布'), (2, '未发布'), (3, '草稿'), (4, '下架'), (5, '已删除')], verbose_name='商品所属状态')),
            ],
            options={
                'verbose_name': '商品分表一',
                'verbose_name_plural': '商品分表一',
            },
        ),
        migrations.CreateModel(
            name='Goods_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='价格')),
                ('goods_sn', models.CharField(default='', max_length=256, verbose_name='商品sku')),
                ('inventory', models.IntegerField(default=0, verbose_name='库存数')),
                ('purchase_quantity', models.IntegerField(default=0, verbose_name='销售额')),
                ('order', models.IntegerField(default=1, help_text='1为最大，越大越靠前显示', verbose_name='商品显示顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_category', to='Goods.Goods', verbose_name='所属商品')),
            ],
            options={
                'verbose_name': '商品规格',
                'verbose_name_plural': '商品规格',
            },
        ),
        migrations.CreateModel(
            name='Goods_subdivide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synopsis', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品简介')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='商品详情')),
                ('hits', models.IntegerField(default=0, verbose_name='点击数')),
                ('goods_environmental', models.TextField(blank=True, null=True, verbose_name='环保信息')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('si_new', models.BooleanField(default=False, verbose_name='是否为新品')),
                ('spu', models.CharField(max_length=48, verbose_name='商品的spu码')),
                ('goods_subdivide', models.OneToOneField(help_text='减小表读取压力，将商品表进行分表', on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='商品细分字段')),
            ],
            options={
                'verbose_name': '商品分表二',
                'verbose_name_plural': '商品分表二',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='按类别分类', max_length=30, verbose_name='分类名字')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目'), (4, '四级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='Goods.GoodsCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '商品所属类别分类',
                'verbose_name_plural': '商品所属类别分类',
            },
        ),
        migrations.CreateModel(
            name='GoodsImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='goods/images/Goods_images/%Y/%m', verbose_name='商品图片')),
                ('is_imagesis', models.BooleanField(default=False, verbose_name='是否为商品主图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GoodsImages_and_Goods', to='Goods.Goods', verbose_name='商品名')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
        migrations.CreateModel(
            name='GoodsStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='所属装饰风格', max_length=24, verbose_name='所属装饰风格')),
                ('images', models.ImageField(blank=True, null=True, upload_to='goods/images/GoodsStyle/%Y/%m', verbose_name='商品图片')),
                ('is_index', models.BooleanField(verbose_name='是否在首页显示')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '所属装饰风格',
                'verbose_name_plural': '所属装饰风格',
            },
        ),
        migrations.CreateModel(
            name='Idenx_baijiahuayi_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/Idenx_baijiahuayi_little/%Y/%m', verbose_name='首页_摆件-花艺首页商品图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_idenx_baijiahuayi_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '首页_摆件-花艺首页商品图',
                'verbose_name_plural': '首页_摆件-花艺首页商品图',
            },
        ),
        migrations.CreateModel(
            name='Idenx_bihuabeio_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/Idenx_bihuabeio_little/%Y/%m', verbose_name='首页_壁画-北欧首页商品图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_idenx_bihuabeio_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '首页_壁画-北欧首页商品图',
                'verbose_name_plural': '首页_壁画-北欧首页商品图',
            },
        ),
        migrations.CreateModel(
            name='Idenx_shuixin_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/Idenx_shuixin_Large/%Y/%m', verbose_name='首页_水心特色商品大图')),
                ('ord', models.IntegerField(blank=True, choices=[(1, '顺序1'), (2, '顺序2')], null=True, unique=True, verbose_name='图片顺序，1为最前')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_idenx_shuixin_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '首页_水心特色商品大图',
                'verbose_name_plural': '首页_水心特色商品大图',
            },
        ),
        migrations.CreateModel(
            name='Idenx_shuixin_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/Idenx_shuixin_little/%Y/%m', verbose_name='首页_水心特色商品小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_idenx_shuixin_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '首页_水心特色商品小图',
                'verbose_name_plural': '首页_水心特色商品小图',
            },
        ),
        migrations.CreateModel(
            name='IndexImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/IndexImg/%Y/%m', verbose_name='主打商品图片')),
                ('ord', models.IntegerField(choices=[(1, '顺序1'), (2, '顺序2'), (3, '顺序3')], unique=True, verbose_name='图片顺序，1为最前')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_indeximg_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '首页大图推荐商品图',
                'verbose_name_plural': '首页大图推荐商品图',
            },
        ),
        migrations.CreateModel(
            name='Spec_param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='参数名')),
                ('numeric', models.BooleanField(verbose_name='是否是数字类型参数，true或false')),
                ('unit', models.CharField(blank=True, max_length=16, null=True, verbose_name='数字类型参数的单位，非数字类型可以为空')),
                ('is_key', models.BooleanField(help_text='为True会此属性出现在商品详情页规格栏中', verbose_name='是否为关键属性')),
                ('is_color', models.BooleanField(help_text='为True时会出现商品颜色图片上传功能', verbose_name='是否为颜色属性')),
                ('searching', models.BooleanField(verbose_name='是否用于搜索过滤')),
                ('generic', models.BooleanField(verbose_name='此属性是否是用于生产skuID，true或false')),
                ('sort', models.IntegerField(verbose_name='排序，越小权重越高')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.GoodsCategory', verbose_name='商品所属分类id')),
            ],
            options={
                'verbose_name': '规格参数组下的参数名',
                'verbose_name_plural': '规格参数组下的参数名',
            },
        ),
        migrations.CreateModel(
            name='Spec_param_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='参数值')),
                ('images', models.ImageField(blank=True, null=True, upload_to='goods/images/Spec_param_value/%Y/%m', verbose_name='商品图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('spec_param_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Spec_param', verbose_name='参数名')),
                ('subdivide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods_subdivide', verbose_name='关联商品细分表')),
            ],
            options={
                'verbose_name': '商品参数表_参数值',
                'verbose_name_plural': '商品参数表_参数值',
            },
        ),
        migrations.CreateModel(
            name='Spec_param_value_To_Goods_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods_category')),
                ('spec_param_value_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Spec_param_value')),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='专栏名')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/Special/%Y/%m', verbose_name='专栏图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '专栏名',
                'verbose_name_plural': '专栏名',
            },
        ),
        migrations.CreateModel(
            name='SpecialGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Goods', verbose_name='关联的商品')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Goods.Special', verbose_name='关联的专栏')),
            ],
            options={
                'verbose_name': '专栏与商品',
                'verbose_name_plural': '专栏与商品',
            },
        ),
        migrations.CreateModel(
            name='Two_bupiruanshi_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_bupiruanshi_Large/%Y/%m', verbose_name='二级-布艺软饰-顶部大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_bupiruanshi_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-布艺软饰-顶部大图',
                'verbose_name_plural': '二级-布艺软饰-顶部大图',
            },
        ),
        migrations.CreateModel(
            name='Two_bupiruanshi_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_bupiruanshi_little/%Y/%m', verbose_name='二级-布艺软饰-商品小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_bupiruanshi_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-布艺软饰-商品小图',
                'verbose_name_plural': '二级-布艺软饰-商品小图',
            },
        ),
        migrations.CreateModel(
            name='Two_chuangyijiaju_chuangyijiaju_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_chuangyijiaju_chuangyijiaju_little/%Y/%m', verbose_name='二级-创意家具-创意家具小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_chuangyijiaju_chuangyijiaju_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-创意家具-创意家具小图',
                'verbose_name_plural': '二级-创意家具-创意家具小图',
            },
        ),
        migrations.CreateModel(
            name='Two_chuangyijiaju_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_chuangyijiaju_Large/%Y/%m', verbose_name='二级-创意家具-顶部大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_chuangyijiaju_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-创意家具-顶部大图',
                'verbose_name_plural': '二级-创意家具-顶部大图',
            },
        ),
        migrations.CreateModel(
            name='Two_chuangyijiaju_shisahngxinying_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_chuangyijiaju_shisahngxinying_Large/%Y/%m', verbose_name='二级-创意家具-时尚新颖大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_chuangyijiaju_shisahngxinying_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-创意家具-时尚新颖大图',
                'verbose_name_plural': '二级-创意家具-时尚新颖大图',
            },
        ),
        migrations.CreateModel(
            name='Two_chuangyijiaju_shisahngxinying_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_chuangyijiaju_shisahngxinying_little/%Y/%m', verbose_name='二级-创意家具-时尚新颖小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_chuangyijiaju_shisahngxinying_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-创意家具-时尚新颖小图',
                'verbose_name_plural': '二级-创意家具-时尚新颖小图',
            },
        ),
        migrations.CreateModel(
            name='Two_chuangyishenghuo_chuangyishenghuo_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_chuangyishenghuo_chuangyishenghuo_little/%Y/%m', verbose_name='二级-创意家具-创意生活小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_chuangyishenghuo_chuangyishenghuo_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-创意家具-创意生活小图',
                'verbose_name_plural': '二级-创意家具-创意生活小图',
            },
        ),
        migrations.CreateModel(
            name='Two_nayixiangxun_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_nayixiangxun_Large/%Y/%m', verbose_name='二级-蜡艺香薰-顶部大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_nayixiangxun_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-蜡艺香薰-顶部大图',
                'verbose_name_plural': '二级-蜡艺香薰-顶部大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_langmanmeishi_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_langmanmeishi_Large/%Y/%m', verbose_name='二级-墙饰壁挂-雅致中式大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_langmanmeishi_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-浪漫美式大图',
                'verbose_name_plural': '二级-墙饰壁挂-浪漫美式大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_langmanmeishi_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_langmanmeishi_little/%Y/%m', verbose_name='二级-墙饰壁挂-雅致中式小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_langmanmeishi_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-浪漫美式小图',
                'verbose_name_plural': '二级-墙饰壁挂-浪漫美式小图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_Large/%Y/%m', verbose_name='二级-墙饰壁挂-顶部大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-顶部大图',
                'verbose_name_plural': '二级-墙饰壁挂-顶部大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_noqiangashi_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_noqiangashi_Large/%Y/%m', verbose_name='二级-墙饰壁挂-浓情欧式大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_noqiangashi_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-浓情欧式大图',
                'verbose_name_plural': '二级-墙饰壁挂-浓情欧式大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_noqiangashi_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_noqiangashi_little/%Y/%m', verbose_name='二级-墙饰壁挂-浓情欧式小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_noqiangashi_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-浓情欧式小图',
                'verbose_name_plural': '二级-墙饰壁挂-浓情欧式小图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiandai_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiandai_Large/%Y/%m', verbose_name='二级-墙饰壁挂-简约现代大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiandai_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-简约现代大图',
                'verbose_name_plural': '二级-墙饰壁挂-简约现代大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiandai_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiandai_little/%Y/%m', verbose_name='二级-墙饰壁挂-简约现代小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiandai_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-简约现代小图',
                'verbose_name_plural': '二级-墙饰壁挂-简约现代小图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiangxunjingyou_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiangxunjingyou_Large/%Y/%m', verbose_name='二级-蜡艺香薰-香薰精油大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiangxunjingyou_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-蜡艺香薰-香薰精油大图',
                'verbose_name_plural': '二级-蜡艺香薰-香薰精油大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiangxunjingyou_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiangxunjingyou_little/%Y/%m', verbose_name='二级-蜡艺香薰-香薰精油小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiangxunjingyou_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-蜡艺香薰-香薰精油小图',
                'verbose_name_plural': '二级-蜡艺香薰-香薰精油小图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiangxunlu_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiangxunlu_Large/%Y/%m', verbose_name='二级-蜡艺香薰-香薰炉大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiangxunlu_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-蜡艺香薰-香薰炉大图',
                'verbose_name_plural': '二级-蜡艺香薰-香薰炉大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_xiangxunlu_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_xiangxunlu_little/%Y/%m', verbose_name='二级-蜡艺香薰-香薰炉小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_xiangxunlu_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-蜡艺香薰-香薰炉小图',
                'verbose_name_plural': '二级-蜡艺香薰-香薰炉小图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_zhiyazhongshi_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_zhiyazhongshi_Large/%Y/%m', verbose_name='二级-墙饰壁挂-雅致中式大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_zhiyazhongshi_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-雅致中式大图',
                'verbose_name_plural': '二级-墙饰壁挂-雅致中式大图',
            },
        ),
        migrations.CreateModel(
            name='Two_qiangshibigua_zhiyazhongshi_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_qiangshibigua_zhiyazhongshi_little/%Y/%m', verbose_name='二级-墙饰壁挂-雅致中式小图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_qiangshibigua_zhiyazhongshi_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-墙饰壁挂-雅致中式小图',
                'verbose_name_plural': '二级-墙饰壁挂-雅致中式小图',
            },
        ),
        migrations.CreateModel(
            name='Two_zhuanshibianjian_Large',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_zhuanshibianjian_Large/%Y/%m', verbose_name='二级-装饰摆件-顶部大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_zhuanshibianjian_large_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-装饰摆件-顶部大图',
                'verbose_name_plural': '二级-装饰摆件-顶部大图',
            },
        ),
        migrations.CreateModel(
            name='Two_zhuanshibianjian_little',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('images', models.ImageField(unique=True, upload_to='goods/images/two_zhuanshibianjian_little/%Y/%m', verbose_name='二级-装饰摆件-推荐大图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_two_zhuanshibianjian_little_related', to='Goods.Goods', verbose_name='所属具体商品')),
            ],
            options={
                'verbose_name': '二级-装饰摆件-推荐小图',
                'verbose_name_plural': '二级-装饰摆件-推荐小图',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Goods_and_GoodsCategory', to='Goods.GoodsCategory', verbose_name='所属类别'),
        ),
        migrations.AddField(
            model_name='goods',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodsstyle', to='Goods.GoodsStyle', verbose_name='所属装饰风格'),
        ),
    ]
