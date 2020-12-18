# *** coding: utf-8 ***
#@Time   : 2020/11/28 4:34 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : conftest.py

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')
        item._nodeid = item.nodeid.encode().decode('unicode_escape')
