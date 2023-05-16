
username = 'admin'
password = 'secret'
host = '192.168.0.113'
port = 50053


result = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds_daily_factor",
        factor_codes=['Day_Yield'],
        start=date(2018, 1, 1),
        end=date(2023, 3, 7),
        securities=['000001_OF']
    )

print(result)