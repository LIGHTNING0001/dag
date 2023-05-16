import random
from datetime import date, timedelta

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

add_position_col_data = DataFrame({
            "date": [date(2022, 3, 9), date(2022, 3, 10), date(2022, 3, 11)],
            "identity": [["000071_OF", "001", "456787_PF"], ["000071_OF", "002", "456249_PF"], ["000071_OF", "003", "456249_PF"]],
            "share": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            "weight": [[0.2, 0.0, 0.8], [0.3, 0.1, 0.3], [0.2, 0.1, 0.2]],
            "amount": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
            "Fund_CNPF_Chara_Adj_NAV": [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]],
            "tradeFee": [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
})

# 上传barbeyond 持仓
engine.portfolio.upload_add_position(
    table_name="aShare_portfolios_fund",
    portfolio_id="tof_case_backing",
    add_position_col_data=add_position_col_data
)

add_net_like_data=DataFrame({
    "date": [date(2022, 3, 9)],
    "cash": [0.0],
    "cashWeight": [0.0],
    "netValue": [0.0],
    "Fund_Day_Yield": [0.04],
    "scale": [0.0],
    "Fund_CNPF_Chara_Adj_NAV": [0.5]
})

engine.portfolio.upload_add_net_like(
    table_name="aShare_portfolios_fund",
    portfolio_id="tof_case_backing",
    add_net_like_data=add_net_like_data
)


# result = engine.portfolio.floor_query_net_like(
#     table_name="aShare_portfolios_fund",
#     portfolio_id="tof_case_02_private",
#     net_like_cols=["Fund_CNPF_Chara_Adj_NAV"],
#     query_date=date(2022, 3, 11)
# )
#
# print(result)
#
# result = engine.portfolio.floor_query_position(
#     table_name="aShare_portfolios_fund",
#     portfolio_id="tof_case_02_private",
#     position_cols=["weight"],
#     query_day=date(2022, 3, 11)
# )
#
# print(result)

schema = engine.portfolio.query_schema(table_name="aShare_portfolios_fund")
print(schema.net_like_cols)
print(schema.position_like_cols)





