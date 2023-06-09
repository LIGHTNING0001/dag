import pymysql
import yaml
import os

# 配置文件应该和当前文件的包在同一级目录
filepath = os.path.dirname(os.path.realpath(__file__)) + "/../"
yamlPath = os.path.join(filepath, "datasouce.yaml")

print(filepath)

with open(yamlPath, 'r', encoding='utf-8') as f:
    config = f.read()

d = yaml.load(config, Loader=yaml.FullLoader)  # 用load方法转字典
config = d['mysql']


def conn():
    connect = pymysql.connect(host=config['host'],
                              port=int(config['port']),
                              user=config['username'],
                              password=config['password'])
    cursor = connect.cursor()
    return connect, cursor


def session(func):
    def wrapper(*args, **kwargs):

        # 获取函数名字，应该是使用__name__属性
        if func.__name__ == 'query':
            connect, cursor = conn()
            cursor.execute(*args)
            result_set = cursor.fetchall()
            connect.close()
            cursor.close()
            return result_set
        elif func.__name__ == 'upsert':
            try:
                connect, cursor = conn()
                cursor.execute(*args)
                connect.commit()
            except Exception as e:
                print(e)
                connect.rollback()
            finally:
                cursor.close()
                connect.close()

    return wrapper


@session
def query(sql):
    pass


@session
def upsert(sql):
    pass
