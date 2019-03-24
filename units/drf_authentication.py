# from rest_framework.authentication import BaseAuthentication
# import jwt
#
# #认证功能
# class Auth(BaseAuthentication):
#     def authenticate(self, request):
#         token =request.META.get("HTTP_AUTHORIZATION")
#         if token:
#             try:
#                 token=token[10:-1]
#                 token_user = jwt.decode(token, 'secret', algorithms=['HS256'])
#                 user_id = token_user.get('id')
#                 user_name = token_user.get('name')
#                 return str(user_id), user_name
#             except BaseException:
#                 return None, None
#         else:
#             return None, None
#
#
# #用户权限功能
# class Auth_permission():
#     def has_permission(self, request, xxx):
#         if request.user!=None:
#             user_id = request.data.get("user_id")
#             request_user = request.user
#             if user_id == request_user:
#                 return True
#             else:
#                 return False
#         else:
#             return False
