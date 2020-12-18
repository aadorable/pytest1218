# *** coding: utf-8 ***
#@Time   : 2020/11/28 7:57 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_pay.py

import requests
import allure
from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder
from api.apiPay import ApiPay

class TestPay():
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 登录系统
        ApiLogin().login_success(self.session)
        # 下订单
        ApiOrder().order(self.session)
        # 实例化支付对象
        self.pay_obj = ApiPay()

    @allure.feature('支付功能')
    @allure.story('支付成功')
    @allure.title('支付成功的测试用例')
    @allure.severity('blocker')
    @allure.testcase('https://blog.csdn.net/adorable_/article/details/110087878', name='☝ 缺陷跟踪列表☝')
    def test_pay(self):
        '''
        支付的测试用例
        :return:
        '''
        resp = self.pay_obj.pay(self.session)
        assert '支付成功' in resp.text