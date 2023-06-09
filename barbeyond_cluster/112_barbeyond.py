import datetime
from datetime import date

import pandas as pd
from pandas import DataFrame
from sdk.client_builder import create_grpc_sdk
import matplotlib.pyplot as plt



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行

username = 'admin'
password = 'secret'
# host = '192.168.0.112'
# port = 50053

# apex-stag1
# host = '192.168.0.100'
# port = 44968

# # 241
# host = '192.168.194.241'
# port = 50053

# 中建投
# host = '101.68.73.4'
# port = 50053


# 241
host = '192.168.194.241'
port = 50053


engine = create_grpc_sdk(username=username, password=password, host=host, port=port)

# result = engine.daily_factor.query_daily_factor(
#         table_name="aShare_stocks_daily_factor",
#         factor_codes=['excess_day_yield_basic', 'avg_excess_day_yield_1m_basic', 'negative_month_yield_pick', 'Return_Monthly1'],
#         start=date(2023, 2, 7),
#         end=date(2023, 3, 7),
#         securities=['000001']
#     )
#
# print(result)


# result = engine.daily_factor.query_daily_factor(
#         table_name="aShare_funds",
#         factor_codes=['Fund_CNPF_Chara_Adj_NAV', 'Fund_Day_Yield'],
#         start=date(2023, 1, 1),
#         end=date(2023, 5, 22),
#         securities=['000001_OF']
#     )
#
# print(result)
#
# net_like = engine.portfolio.floor_query_net_like(
#         table_name="composite_benchmark",
#         portfolio_id="benchmarkCode591577942818315",
#         net_like_cols=['Fund_Day_Yield', 'Return_Monthly'],
#         query_date=date(2023, 1, 31),
# )
#
# print("组合：", net_like.head(40))


# bin = engine.daily_factor.purify_dry_run(
#     table_name="aShare_stocks_daily_factor",
#     factor_codes=["Return_Weekly_1"],
#     keep_count=1
# )
#
# print(bin)
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


# macro_value = engine.macro.query_by_days(
#         "aShare_macros",
#         ['macro_cost_risk_free', 'FreeRisk_Interest_Monthly1'],
#         date_generate("2000-01-01", "2023-03-09")
# )
#
# print(macro_value)

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
#
# single_date_sparse_client = engine.sparse.single_date
# query_result = single_date_sparse_client.query_data_by_stock_and_offset("aShare_stocks_month", ["000001"], ['avg_excess_day_yield_1wm'],
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
#     from_date=date(2005, 1, 1),
#     to_date=date(2022, 1, 1)
# )
#
# print(stock_unv)

# 全市场，全基金 =》 构建投资组合权重 =》 形成投资组合

# 特征：1. 近一年历史新低

def fetch_all_fund():

    all_funds = engine.identity.query_all_identity('aShare_funds')

    for f in all_funds['code']:

        result = engine.daily_factor.query_daily_factor(
            table_name="aShare_funds",
            factor_codes=['Fund_Day_Yield'],
            start=date(2005, 1, 1),
            end=date(2023, 6, 8),
            securities=[f]
        )


if __name__ == '__main__':

    result = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_CNPF_Chara_Adj_NAV'],
        start=date(2010, 1, 1),
        end=date(2023, 6, 8),
        securities=['005693_OF']
    )

    print(result)

    plt.plot(result['tradingDay'], result['Fund_CNPF_Chara_Adj_NAV'])

    plt.title(result['code'][0])
    plt.xlabel('日期')
    plt.ylabel('收益')

    # 显示图形
    plt.show()
