from datetime import date

from client.grpc_client import engine

if __name__ == '__main__':

    result = engine.daily_factor.query_daily_factor(
        table_name='aShare_funds',
        factor_codes=['Fund_Day_Yield'],
        start=date(2005, 1, 4),
        end=date(2023, 2, 2),
        securities=['000001_OF'])

    print(result)

