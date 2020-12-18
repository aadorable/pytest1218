# *** coding: utf-8 ***
#@Time   : 2020/11/28 5:27 下午
#@Author : xueqing.wu
#@Email  : wuxueqing@126.com
#@File   : pymysqltools.py

import pymysql
from tools.logger import GetLogger

logger = GetLogger.get_logger()

class DataBaseHandle():
    def __init__(self, database):
        '''
        连接数据库初始化
        '''
        self.ip = '10.8.7.179'
        self.username = 'root'
        self.password = '123456'
        self.database = database
        self.port = 3306
        self.db = pymysql.connect(self.ip, self.username, self.password, self.database, self.port)

    def insertDb(self, sql):
        '''
        插入数据
        :param sql: sql语句
        :return:
        '''
        # 获取游标
        cur = self.db.cursor()
        try:
            # 执行sql语句
            cur.execute(sql)
            # 对数据进行提交
            self.db.commit()
        except Exception as e:
            logger.error('insert data erro：{}'.format(e))
            self.db.rollback()  # 发生错误时回滚
        finally:
            cur.close()

    def deleteDb(self, sql):
        '''
        删除数据
        :param sql: sql语句
        :return:
        '''
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            self.db.commit()
        except Exception as e:
            logger.error('delete data error：{}'.format(e))
            self.db.rollback()
        finally:
            cur.close()

    def updateDb(self, sql):
        '''
        修改数据
        :param sql: sql语句
        :return:
        '''
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            self.db.commit()
        except Exception as e:
            logger.error('update data error：{}'.format(e))
            self.db.rollback()
        finally:
            cur.close()

    def selectDb(self, sql):
        '''
        数据库查询操作
        :param sql: 查询的sql语句
        :return: 查询出来的数据
        '''
        # 建立一个游标
        cur = self.db.cursor()
        try:
            # 执行sql语句，结果保存在游标中
            cur.execute(sql)
            # 从游标中获取数据
            data = cur.fetchall()
            return data
        except Exception as e:
            logger.error('select data error：{}'.format(e))
            raise e
        # 无论是否查询有误，都需要关闭游标
        finally:
            cur.close()

    def closeDb(self):
        '''
        关闭数据库连接
        :return:
        '''
        self.db.close()


if __name__ == '__main__':
    db = DataBaseHandle('mtx')
    sql = 'select username,pwd from s_user where username="xueqing" or username="shamo"'
    print(db.selectDb(sql))