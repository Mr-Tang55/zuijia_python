"""zuijia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from  rest_framework.routers import DefaultRouter

from apps.Goods.views import *
#xadmin文档设置
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

# router= DefaultRouter()

# router.register(r'style',Style,base_name='category')

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^admin/',  include(xadmin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='api-auth')),
    url(r'^docs/', include_docs_urls(title='最家家具')),
    url(r'^index/', Index.as_view({'get':'list'}),name='index'),
    url(r'^style/(?P<pk>\d+)/$', Style.as_view({'get':'list'}),name='style'),
    url(r'', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #没有这一句无法显示上传的图片


