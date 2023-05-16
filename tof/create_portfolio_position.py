

import datetime
import random
import time
from datetime import date, timedelta
from functools import reduce

import pymysql
from pandas import DataFrame
from sdk.client_builder import create_grpc_sdk
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

username = 'admin'
password = 'secret'

host = '192.168.0.100'
port = 44968

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)

host = '192.168.0.100'
port = 50405
username = 'root'
password = 'beifa888'

db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()

sql = "select code from jictrust_betalpha.fund_of_info limit 100"
cursor.execute(sql)
result_set = cursor.fetchall()
all_code = []
for item in result_set:
    all_code.append(item[0])

print(all_code)

all_code = ["560002_OF", "456124_PF"]

sql = "select trading_date from jictrust_saas.trading_day where trading_date between '2022-03-08' and '2022-03-19'"
cursor.execute(sql)
result_set = cursor.fetchall()
all_date = []
for item in result_set:
    all_date.append(item[0])

print(all_date)

all_date = [date(2022, 3, 14), date(2022, 3, 15)]

portfolio_id = "tof_case_18"
identity = []
share = []
weight = []
amount = []
value = []
tradeFee = []
for d in all_date:
    identity.append(all_code)
    share.append([0.0] * len(all_code))
    weight.append([1/len(all_code)] * len(all_code))
    amount.append([0.0] * len(all_code))
    value.append([1.0] * len(all_code))
    tradeFee.append([0.0] * len(all_code))

add_position_col_data = DataFrame({
            "date": all_date,
            "identity": identity,
            "share": share,
            "weight": weight,
            "amount": amount,
            "Fund_CNPF_Chara_Adj_NAV": value,
            "tradeFee": tradeFee
})

engine.portfolio.upload_add_position(
    table_name="aShare_portfolios_fund",
    portfolio_id=portfolio_id,
    add_position_col_data=add_position_col_data
)

add_net_like_data=DataFrame({
    "date": [date(2022, 3, 14)],
    "cash": [0.0],
    "cashWeight": [0.0],
    "netValue": [0.0],
    "Fund_Day_Yield": [0.04],
    "scale": [0.0],
    "Fund_CNPF_Chara_Adj_NAV": [0.5]
})

engine.portfolio.upload_add_net_like(
    table_name="aShare_portfolios_fund",
    portfolio_id=portfolio_id,
    add_net_like_data=add_net_like_data
)