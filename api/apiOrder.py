# *** coding: utf-8 ***
#@Time   : 2020/11/28 5:51 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : apiOrder.py

import settings
from settings import IP, HEADERS
from tools.logger import GetLogger

logger = GetLogger().get_logger()

class ApiOrder():
    def __init__(self):
        logger.info('开始获取下订单接口的url')
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info('下订单接口的url是：{}'.format(self.url))

    def order(self, session):
        '''
        发起下订单请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 8,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 51,
            'payment_id': 1,
            'spec': ''
        }
        logger.info('开始发起下订单请求，请求的参数是{}，请求头是{}'.format(data, HEADERS))
        resp_order = session.post(self.url, data=data, headers=HEADERS)
        logger.info('响应的结果是{}'.format(resp_order.json()))
        # 将产生的数据放在settings中
        settings.JUMP_URL = resp_order.json().get('data').get('jump_url')
        return resp_order