from datetime import date

from sdk.client_builder import create_grpc_sdk

username = 'admin'
password = 'secret'

# 中建投
host = '101.68.73.4'
port = 50053

# 241 环境
# host = '192.168.194.241'
# port = 50053

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)



result = engine.identity.query_all_identity(table_name="aShare_benchmarks")
funds = result['code'].tolist()
print('barbeyond benchmarks code :', len(funds), funds)


for item in funds:

    result = engine.daily_factor.query_daily_factor(
        table_name="aShare_benchmarks",
        factor_codes=['return_monthly'],
        start=date(2023, 3, 13),
        end=date(2023, 3, 22),
        securities=['item']
    )
    print(result)










