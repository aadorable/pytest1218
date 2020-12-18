# *** coding: utf-8 ***
#@Time   : 2020/11/28 4:34 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : settings.py

import os

IP = 'http://10.8.4.129'
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)
JUMP_URL = None