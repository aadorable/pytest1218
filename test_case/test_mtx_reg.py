# *** coding: utf-8 ***
#@Time   : 2020/11/28 6:47 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : test_mtx_reg.py

import requests
import pytest
import allure
from api.apiReg import ApiReg
from tools.pymysqltools import DataBaseHandle
from tools.readData import ReadData
from tools.logger import GetLogger
from faker import Faker
from settings import DIR_NAME

all_cases = ReadData().get_csv('reg.csv')
ids = []
for case in all_cases:
    ids.append(case[5])

class TestReg():
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 实例化注册借口对象
        self.reg_obj = ApiReg()
        # 实例化数据库对象
        self.db = DataBaseHandle('mtx')
        self.logger = GetLogger().get_logger()

    def teardown_class(self):
        '''
        测试结束关闭数据库
        :return:
        '''
        self.db.closeDb()

    @allure.feature('注册功能')
    @allure.story('注册成功')
    @allure.title('注册成功的测试用例')
    @allure.severity('blocker')
    @allure.description('关于注册成功的测试用例')
    @allure.issue('https://blog.csdn.net/adorable_/article/details/110087878', name='☝缺陷跟踪列表☝')
    def test_reg_success(self):
        fake = Faker()
        username = fake.first_name()
        body = {
            'accounts': username,
            'pwd': 123456,
            'type': 'username',
            'is_agree_agreement': 1
        }
        resp = self.reg_obj.reg(self.session, body)
        sql = 'select username,pwd from s_user where username="{}"'.format(username)
        data = self.db.selectDb(sql)
        self.logger.info('数据库查询的数据为：{}'.format(data))
        assert resp.json()['msg'] == '注册成功'
        assert data[0][0] == username

    @allure.feature('注册功能')
    @allure.story('注册失败')
    @allure.title('注册失败的测试用例')
    @allure.severity('critical')
    @allure.description_html('<h3>关于注册失败的一些测试用例</h3>')
    @allure.testcase('https://blog.csdn.net/adorable_/article/details/110087878', name='☝ 缺陷跟踪列表☝')
    @pytest.mark.parametrize('username, password, type, is_agree_agreement, exp, ids', all_cases, ids=ids)
    def test_reg_fail(self, username, password, type, is_agree_agreement, exp, ids):
        body = {
            'accounts': username,
            'pwd': password,
            'type': type,
            'is_agree_agreement': is_agree_agreement
        }
        resp = self.reg_obj.reg(self.session, body)
        assert resp.json()['msg'] == exp
        with open(DIR_NAME + '/test_data/reg.csv') as f:
            content = f.read()
            allure.attach(content, '注册接口的测试数据', allure.attachment_type.CSV)
