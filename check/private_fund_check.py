import datetime
from datetime import date

from sdk.client_builder import create_grpc_sdk
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)


username = 'admin'
password = 'secret'

# 中建投
host = '101.68.73.4'
port = 50053


engine = create_grpc_sdk(username=username, password=password, host=host, port=port)
private_funds = engine.identity.query_all_identity(table_name="aShare_private_funds")

codes = []
for index, row in private_funds.iterrows():
    result = engine.daily_factor.query_daily_factor(
        table_name="aShare_private_funds",
        factor_codes=['Fund_Day_Yield', 'Fund_CNPF_Chara_Adj_NAV'],
        start=date(1996, 3, 1),
        end=row['startDate'],
        securities=[row['code']]
    )

    if len(result['Fund_Day_Yield'].tolist()) != 0:
        print(row['code'])
        codes.append(row['code'])

print(codes)