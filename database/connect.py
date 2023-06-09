import pymysql
import yaml
import os

filepath = os.path.dirname(os.path.realpath(__file__)) + "/../"
yamlPath = os.path.join(filepath, "datasouce.yaml")

print(filepath)

with open(yamlPath, 'r', encoding='utf-8') as f:
    config = f.read()

d = yaml.load(config, Loader=yaml.FullLoader)  # 用load方法转字典
config = d['mysql']

# connect = pymysql.connect(host=config['host'], port=config['port'], user=config['username'],password=config['password'])

def conn():

    connect = pymysql.connect(host=config['host'], port=config['port'], user=config['username'],
                              password=config['password'])
    cursor = connect.cursor()

    return connect, cursor

def session(function):
    def wrapper(*args, **kwargs):
        if function == 'query':
            connect, cursor = conn()
            cursor.execute(*args)
            result_set = cursor.fetchall()
            connect.close()
            cursor.close()
            return result_set
        elif function == 'upsert':
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



result_set = query("select * from barbeyond.t_data_logic_table_col")
print(result_set)
upsert("update barbeyond.t_data_logic_table_col set init_start = '2023-01-02' where full_code = 'stock.factor.annual_return_std_monthly_1m'")
