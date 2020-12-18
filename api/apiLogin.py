# *** coding: utf-8 ***
#@Time   : 2020/11/28 5:50 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiLogin.py

from settings import IP, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiLogin():
    def __init__(self):
        logger.info('开始获取登录接口的url')
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'
        logger.info('登录接口的url是：{}'.format(self.url))

    def login(self, session, data):
        '''
        登录接口的测试
        :param session:
        :param data: 请求参数
        :return:
        '''
        logger.info('开始发起登录请求，请求的参数是{}，请求头是{}'.format(data, HEADERS))
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        logger.info('响应的结果是{}'.format(resp_login.json()))
        return resp_login

    def login_success(self, session):
        '''
        登录成功的接口，用于测试有关联的接口
        :param session:
        :return:
        '''
        data = {
            'accounts': 'xueqing',
            'pwd': '123456'
        }
        logger.info('开始发起登录请求，请求的参数是{}，请求头是{}'.format(data, HEADERS))
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        logger.info('响应的结果是{}'.format(resp_login.json()))
        return resp_login