import datetime
import re
import time

import pymysql
import paramiko

import pandas as pd

from barbeyond_cluster.factor_meta import FactorMeta

host = '192.168.0.113'
port = 3306
username = 'root'
password = 'beifa888'

db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()


def insert_day_yield_to_result():
    path = '/home/betalpha/app/jar/cluster_server/data/cache/daily_factor/aShare_stocks_daily_factor/upload-zone/identity'

    trans = paramiko.Transport(("192.168.0.112", 22))
    trans.connect(username="betalpha", password="bfisnotgf")

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    command = "cat {}".format(path)
    print(command)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)

    lines = ssh_stdout.readlines()

    identities = [i.rstrip('\n') for i in lines]

    print(identities)

    # 关闭连接
    trans.close()

    for identity in identities:
        items = identity.split(',')
        item = items[0]
        start_date = items[1]
        end_date = '2023-03-07' if items[2] == '' else items[2]

        sql = "insert into barbeyond.t_scheduler_data_update_result values('stock.factor.Day_Yield', '{}', '{}', '{}'," \
              " '1680092558802', '1680092558802')".format(item, start_date, end_date)

        cursor.execute(sql)
        db.commit()
    cursor.close()
    db.close()


# sparse factor add meta info
def add_factor_meta():
    sql = "insert into barbeyond.t_factor_meta(data_col_id, time_unit, create_user_id, update_user_id) " \
          "select data_col_id, case when data_physical_table_id = 11 then 'EMD' " \
          "when data_physical_table_id = 12 then 'EYD' end as time_unit, 1, 1 from t_data_logic_table_col " \
          "where data_physical_table_id in (11, 12)"

    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def read_excel(file):
    df = pd.read_excel(file)
    items = []
    n = len(df)

    for row in df.iterrows():
        line = []
        line.append(row[1]['name'])
        line.append(row[1]['code'])
        line.append(row[1]['formula'])
        line.append(str(row[1]['timeUnit']))
        items.append(line)

def read_csv(file):
    factors = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            t = re.split(',', line)
            print(t)
            tmp = []
            tmp.append(t[1])
            tmp.append(t[2])
            tmp.append(t[3])
            tmp.append(t[4])
            tmp.append(t[7])
            tmp.append(t[8])
            factors.append(tmp)

    return factors[1:]

class Factor:

    def __init__(self, namespace, name, code, formula, timeUnit, initStart):
        self.full_code = namespace + "." + code
        self.code = code
        self.name = name
        self.formula = formula
        self.timeUnit = (FactorMeta.EYD if 'EYD' == timeUnit else FactorMeta.EMD)
        self.initStart = initStart


def insert_meta_data():
    file = '/Users/mac/PycharmProjects/dag_v2_test/cluster_factor_v2.csv'
    factor_line = read_excel(file)

    for row in factor_line:
        factor = Factor(row[0], row[1], row[2], row[3], row[4], row[5])

        sql = "insert into barbeyond.t_data_logic_table_col(data_logic_table_id, code, " \
              "full_code, name, desc, formula, init_start, data_constraint_id, data_physical_table_id, data_middle_logic_table_id," \
              "data_col_extra_info_table_id, create_user_id, update_time, update_user_id, create_time) " \
              "values ({}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(
            1, factor.code, factor.full_code, factor.name, '', factor.formula, factor.initStart, -1, factor.timeUnit, -1, -1, 1,
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), -1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        )

        print(sql)

        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()








if __name__ == '__main__':

    # sql = "insert into barbeyond.t_factor_meta(data_col_id, time_unit, create_user_id, update_user_id) " \
    #       "select data_col_id, case when data_physical_table_id = 11 then 'EMD' " \
    #       "when data_physical_table_id = 12 then 'EYD' end as time_unit, 1, 1 from t_data_logic_table_col " \
    #       "where data_physical_table_id in (11, 12)"
    #
    # print(sql)
    # add_factor_meta()

    insert_meta_data()
