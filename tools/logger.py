# *** coding: utf-8 ***
#@Time   : 2020/11/28 5:15 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : logger.py

import logging.handlers
from settings import DIR_NAME

class GetLogger():
    # 单例模式，只生成一个logger对象
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            # 1. 获取日志器
            cls.logger = logging.getLogger()
            # 2. 设置总级别
            cls.logger.setLevel(logging.INFO)
            # 3. 设置格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] -%(message)s'
            fm = logging.Formatter(fmt)
            # 4. 获取处理器
            tf = logging.handlers.TimedRotatingFileHandler(filename=DIR_NAME + '/Logs/mtx.log',
                                                           when='S',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 5. 将格式器添加到处理器中
            tf.setFormatter(fm)
            # 6. 将处理器添加到日志器中
            cls.logger.addHandler(tf)
        return cls.logger


if __name__ == '__main__':
    logger = GetLogger().get_logger()
    logger.debug('调试')
    logger.info('信息')
    logger.error('错误')