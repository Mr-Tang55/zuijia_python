from rest_framework.pagination import PageNumberPagination

#分页功能
class Goods_Pagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 1
    # 设置URL分页参数
    page_size_query_param = 'page_size'
    # 获取URL参数中传入的页码
    page_query_param = "page"
    # 最大支持的每页显示的数据条数
    max_page_size = 100