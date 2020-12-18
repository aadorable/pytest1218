# *** coding: utf-8 ***
#@Time   : 2020/11/28 7:44 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiPay.py

import settings

class ApiPay():
    def __init__(self):
        self.url = settings.JUMP_URL

    def pay(self, session):
        # 对302接口禁止重定向 allow_redirects=False
        resp = session.get(self.url, allow_redirects=False)
        # 提取形影头中的location，对location后面的地址发起请求
        resp_pay = session.get(resp.headers['location'])
        return resp_pay
