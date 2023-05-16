import datetime
from datetime import date

from pandas import DataFrame
from sdk.client_builder import create_grpc_sdk

username = 'admin'
password = 'secret'
host = '192.168.0.112'
port = 50053

# apex-stag1
# host = '192.168.0.100'
# port = 44968

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)
result = engine.daily_factor.query_daily_factor(
        table_name="aShare_stocks_daily_factor",
        factor_codes=['Day_Yield', 'd2'],
        start=date(2005, 1, 4),
        end=date(2006, 3, 7),
        securities=['000001']
    )

print(result.tail(20))


bin = engine.daily_factor.purify_dry_run(
    table_name="aShare_stocks_daily_factor",
    factor_codes=["Return_Weekly_1"],
    keep_count=1
)

print(bin)
#
# all = engine.trading_day.query_all_trading_day("aShare_stocks_daily_factor")
# print(all)


def date_generate(start_date, end_date):
    start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    next_dt = start_dt

    date_list = []
    while next_dt <= end_dt:
        next_dt_str = next_dt.date()
        date_list.append(next_dt_str)
        next_dt = next_dt + datetime.timedelta(days=1)

    return date_list


macro_value = engine.macro.query_by_days(
        "aShare_index",
        ["idx_000906sh"],
        date_generate("2000-01-01", "2023-03-09")
)

print(macro_value)


# username = 'admin'
# password = 'secret'
# host = '192.168.0.112'
# port = 50053
#
# engine = create_grpc_sdk(username=username, password=password, host=host, port=port)
# engine.macro.save_macro(
#     "aShare_index",
#     ["idx_000906sh"],
#     macro_value
# )

# single_date_sparse_client = engine.sparse.single_date
# query_result = single_date_sparse_client.query_data_by_stock_and_offset("aShare_stocks_year", ["000001"], ['return_std_daily_wyd'],
#                                                                             date(2023, 2, 2), 0)
# print(query_result)
#
# factor_list = single_date_sparse_client.query_origin_data_by_stock_release_date(
#     table='aShare_stocks_month',
#     stocks=["000001"],
#     factor_cols=['return_std_daily_wmd', 'annual_ret_daily_wmd'],
#     from_date=date(2010, 1, 1),
#     to_date=date(2023, 3, 1)
# )
#
# print(factor_list)
#
# factor_list = single_date_sparse_client.query_origin_data_by_stock_release_date(
#     table='aShare_stocks_year',
#     stocks=["000001"],
#     factor_cols=['return_std_daily_wyd'],
#     from_date=date(2010, 1, 1),
#     to_date=date(2023, 5, 1)
# )
#
# print(factor_list)

# stock_unv = engine.universe.query_universe_by_date_range(
#     "aShare_stocks_universe",
#     "all_a_stock",
#     from_date=date(2022, 1, 1),
#     to_date=date(2023, 1, 1)
# )
#
# print(stock_unv)
