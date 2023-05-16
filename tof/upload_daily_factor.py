import datetime
import random
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

# host = '127.0.0.1'
# port = 50053

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)


host = '192.168.0.100'
port = 50405
username = 'root'
password = 'beifa888'


db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()

sql = "select trading_date from jictrust_saas.trading_day"
cursor.execute(sql)
result_set = cursor.fetchall()
all_date = []
for item in result_set:
    all_date.append(item[0])

table_name = 'aShare_bonds_copy'

# 上传交易日
engine.trading_day.upload_trading_day(
    table_name=table_name,
    days=DataFrame(all_date)
)

codes = ["001"]
startDate = [date(2022, 3, 11)]
endDate = [None]

engine.identity.upload_identity(
    table_name=table_name,
    identities=DataFrame(
        {
            "code": codes,
            "startDate": startDate,
            "endDate": endDate,
        },
    )
)

engine.daily_factor.create_table(table_name=table_name, factor_codes=["Fund_CNPF_Chara_Adj_NAV", "Fund_Day_Yield"])

n = 0
for code in codes:

    start = startDate[n]
    # end = date(2022, 4, 18) if endDate[n] is None else endDate[n]
    end = date(2022, 3, 15)
    sub_trading_day = all_date[all_date.index(start):all_date.index(end)]

    value = []
    for i in range(len(sub_trading_day)):
        value.append(random.uniform(1, 2))

    print(value)
    item_code = [code] * len(sub_trading_day)

    fund_nav = DataFrame({
            "code": item_code,
            "tradingDay": sub_trading_day,
            "Fund_CNPF_Chara_Adj_NAV": value,
        })

    print(fund_nav)

    value1 = []
    for i in range(len(value)):
        if i == 0: value1.append(0.0)
        if i + 1 < len(value):
            value1.append((value[i + 1] - value[i]) / value[i])

    fund_return = DataFrame({
            "code": [code] * len(sub_trading_day),
            "tradingDay": sub_trading_day,
            "Fund_Day_Yield": value1,
    })
    print(fund_return)

    engine.daily_factor.upload_factor(
        table_name=table_name,
        factor_codes=["Fund_CNPF_Chara_Adj_NAV"],
        data_df=fund_nav)

    engine.daily_factor.upload_factor(
        table_name=table_name,
        factor_codes=["Fund_Day_Yield"],
        data_df=fund_return)
    n = n + 1

