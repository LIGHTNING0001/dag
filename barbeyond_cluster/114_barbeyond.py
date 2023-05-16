from datetime import date

from sdk.client_builder import create_grpc_sdk

username = 'admin'
password = 'secret'
host = '192.168.0.114'
port = 50053

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)

result = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_CNPF_Chara_Adj_NAV'],
        start=date(2023, 1, 1),
        end=date(2023, 3, 7),
        securities=['000001_OF']
    )

print(result)
