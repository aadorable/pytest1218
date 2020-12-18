# *** coding: utf-8 ***
#@Time   : 2020/11/28 6:09 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_login.py

import requests
import pytest
import allure
from api.apiLogin import ApiLogin
from tools.readData import ReadData
from settings import DIR_NAME

all_cases = ReadData().get_csv('login_data.csv')
ids = []
for case in all_cases:
    ids.append(case[3])

class TestLogin():
    def setup_class(self):
        # 获取session对象，做cookie处理
        self.session = requests.session()
        # 实例化登录接口对象
        self.login_obj = ApiLogin()

    @allure.feature('登录功能')
    @allure.story('登录的参数：正向和逆向')
    @allure.title('登录的测试用例')
    @allure.severity('critical')
    @allure.description('关于登录的一些测试用例')
    @allure.link('https://blog.csdn.net/adorable_/article/details/110087878')
    @pytest.mark.parametrize('accounts, pwd, exp, ids', all_cases, ids=ids)
    def test_login(self, accounts, pwd, exp, ids):
        data = {
            'accounts': accounts,
            'pwd': pwd
        }
        resp = self.login_obj.login(self.session, data)
        assert resp.json()['msg'] == exp
        with open(DIR_NAME + '/test_data/login_data.csv', encoding='utf-8') as f:
            content = f.read()
            allure.attach(content, '登录接口的测试数据', allure.attachment_type.CSV)


