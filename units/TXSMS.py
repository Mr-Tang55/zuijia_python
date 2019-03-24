# from qcloudsms_py import SmsSingleSender
# from qcloudsms_py.httpclient import HTTPError
# from random import choice
#
# #手机验证码生成
#
# def generate_code():
#     seeds = "1234567890"
#     random_str = []
#     for i in range(6):
#         random_str.append(choice(seeds))
#     return "".join(random_str)
#
# #短信验证码发送
# def TxSms(mobile,code=generate_code()):
#     template_id = 7839  #模版id
#     sms_sign = "最家家具"   #模版签名
#     ssender = SmsSingleSender(1400173997, "a85c60387477b0236ba0e06c24297c41") #APPID和KEY
#     params = [code]  #验证码 模板内容中需要有几个参数，这里就要填写几个
#
#     try:
#         # 签名参数未提供或者为空时，会使用默认签名发送短信
#         result = ssender.send_with_param(86, str(mobile),template_id, params, sign=sms_sign, extend="",ext=code)
#         return result
#     except HTTPError as e:
#         return {"result": 404, "errmsg": "函数调用出错",}
#     except Exception as e:
#         return {"result": 404,"errmsg": "函数调用出错"}
#

