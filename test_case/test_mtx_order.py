# *** coding: utf-8 ***
#@Time   : 2020/11/28 7:27 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_order.py

import requests
import allure
from api.apiOrder import ApiOrder
from api.apiLogin import ApiLogin

class TestOrder():
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 实例化下订单接口对象
        self.order_obj = ApiOrder()
        # 下订单的前提是已经登录系统
        ApiLogin().login_success(self.session)

    @allure.feature('下单功能')
    @allure.story('下单成功')
    @allure.title('成功下单的测试用例')
    @allure.severity('blocker')
    @allure.testcase('https://blog.csdn.net/adorable_/article/details/110087878', name='☝ 缺陷跟踪列表☝')
    def test_order(self):
        '''
        测试下订单接口
        :return:
        '''
        resp = self.order_obj.order(self.session)
        assert resp.json()['msg'] == '提交成功'