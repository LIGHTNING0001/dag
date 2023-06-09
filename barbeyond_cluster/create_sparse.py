import pymysql
from sdk.client_builder import create_grpc_sdk

username = 'admin'
password = 'secret'
host = '192.168.0.112'
port = 50053

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)

# mysql

host = '192.168.0.113'
port = 3306
username = 'root'
password = 'beifa888'

db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()

sql = "select code from barbeyond.t_data_logic_table_col where full_code like 'stock.factor%' and data_physical_table_id = 12"

cursor.execute(sql)
result_set = cursor.fetchall()
codes = []
for item in result_set:
    codes.append(item[0])

engine.sparse.single_date.create_table('aShare_stocks_year', codes)


sql = "select code from barbeyond.t_data_logic_table_col where full_code like 'stock.factor%' and data_physical_table_id = 11"

cursor.execute(sql)
result_set_1 = cursor.fetchall()
print(result_set_1)
codes = []
for item in result_set_1:
    codes.append(item[0])

engine.sparse.single_date.create_table('aShare_stocks_month', list(set(codes)))





