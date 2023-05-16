import datetime
import logging
import math
from datetime import date

from pandas import DataFrame
from sdk.client_builder import create_grpc_sdk

import pandas as pd
import numpy as np

from calculator.formula import cum, g_avg_return_t, std, kurt, skew, linregress

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行


# apex-stag1
# host = '192.168.0.100'
# port = 44968
username = 'admin'
password = 'secret'

# 中建投
# host = '101.68.73.4'
# port = 50053

# 241 环境
host = '192.168.194.241'
port = 50053

# 242 环境
# host = '192.168.194.241'
# port = 50053

# 167 环境
# host = '172.16.60.167'
# port = 50054


# 中建投
# host = '101.68.73.4'
# port = 50053


# apex-stag1
# host = '192.168.0.100'
# port = 44968



log = logging.getLogger(__name__)
log.info("start connecting grpc server... ")
engine = create_grpc_sdk(username=username, password=password, host=host, port=port)


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


if __name__ == '__main__':

    # engine.daily_factor.upload_factor(
    #     table_name='aShare_bonds',
    #     factor_codes=["Fund_CNPF_Chara_Adj_NAV"],
    #     data_df=DataFrame({
    #         "code": ['001'],
    #         "tradingDay": [date(2022, 3, 11)],
    #         "Fund_CNPF_Chara_Adj_NAV": [0.98],
    # }))


    # result = engine.portfolio.floor_query_position(
    #     table_name="aShare_portfolios_fund",
    #     portfolio_id="tof_only_open387418370228833",
    #     position_cols=["weight"],
    #     query_day=date(2022, 3, 11)
    # )
    #
    # print(result)

    # # # Fund_CNPF_Chara_Adj_NAVavg_excess_day_yield_5y
    result = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['positive_month_1m'],
        start=date(2023, 4, 10),
        end=date(2023, 5, 10),
        securities=['000001_OF', '560002_OF', '590007_OF']
    )
    print(result)

    sparse_data = engine.sparse.single_date.query_data_by_stock_and_offset(
        table='aShare_funds_year',
        stocks=['000001_OF', '560002_OF', '590007_OF'],
        factor_cols=['count_d_1wy', 'abret_eyd'],
        query_date=date(2022, 4, 1),
        pre_offset=-1
    )

    print(sparse_data)

    sparse_data = engine.sparse.single_date.query_data_by_stock_and_offset(
        table='aShare_funds_month',
        stocks=['000001_OF', '560002_OF', '590007_OF'],
        factor_cols=['count_d_1wm'],
        query_date=date(2023, 4, 30),
        pre_offset=0
    )

    print(sparse_data)

    v = engine.sparse.single_date.query_origin_data_by_stock_release_date(
        table='aShare_funds_month',
        stocks=['000001_OF'],
        factor_cols=['count_d_1wm'],
        from_date=date(2023, 1, 1),
        to_date=date(2023, 5, 1),
    )

    print(v)

    # tradingDay = result['tradingDay'].tolist()
    #
    # excess_day_yield = result['excess_day_yield'].tolist()
    #
    # result1 = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_funds",
    #     factor_codes=['alpha_daily_1y', 'beta_daily_1y'],
    #     start=date(2023, 4, 12),
    #     end=date(2023, 4, 12),
    #     securities=['000001_OF']
    # )
    # print(result1)

    result1 = engine.daily_factor.query_daily_factor(
        table_name="aShare_benchmarks",
        factor_codes=['month_6m'],
        start=date(2023, 5, 1),
        end=date(2023, 5, 9),
        securities=['idx_000906sh']
    )
    print(result1)


    # exposure_t(excess_day_yield, [Index_Return - macro_cost_risk_free], -inf: 0, D, 1)

    # result = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_private_funds",
    #     factor_codes=['Fund_Day_Yield', "Fund_CNPF_Chara_Adj_NAV"],
    #     start=date(2023, 3, 2),
    #     end=date(2023, 4, 7),
    #     securities=['ZH000025']
    # )
    # print(result)
    #
    #
    # result = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_private_funds",
    #     factor_codes=['Fund_Day_Yield', "Fund_CNPF_Chara_Adj_NAV",
    #                   "history_return_estimate_nav", "history_week_return_estimate_nav", "multi_factor_estimate_nav"],
    #     start=date(2023, 4, 2),
    #     end=date(2023, 4, 7),
    #     securities=['SQR109', 'ZH000025']
    # )
    # print(result)
    #
    # result = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_bonds",
    #     factor_codes=['Fund_Day_Yield'],
    #     start=date(2022, 3, 8),
    #     end=date(2022, 3, 14),
    #     securities=['001']
    # )
    # print(result)

    # returns = result['Funprint()d_Day_Yield'].tolist()
    #
    # returns = cum(returns)
    #
    # result = engine.daily_factor.query_daily_factor(
    #
    #     table_name="aShare_benchmarks",
    #     factor_codes=['maxdrawdown_1m', 'maxdrawdown_3m', 'maxdrawdown_6m', 'maxdrawdown_sinceyear', 'profitlossratio_daily_sincetotal',
    #                   'maxdrawdown_1y', 'maxdrawdown_2y', 'maxdrawdown_3y', 'maxdrawdown_5y', 'maxdrawdown_sincetotal'],
    #     start=date(2023, 1, 4),
    #     end=date(2023, 2, 6),
    #     securities=['idx_000001sh']
    # )
    # print(result)

    # result = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_benchmarks",
    #     factor_codes=['Fund_Day_Yield', 'cummul_day_yield_sincetotal_in_basicposday'],
    #     start=date(2023, 1, 1),
    #     end=date(2023, 3, 7),
    #     securities=['idx_000001sh']
    # )
    # print(result)
    # print(result['Fund_Day_Yield'].tolist())

    #
    # result = engine.daily_factor.query_daily_factor(
    #
    #     table_name="aShare_benchmarks",
    #     factor_codes=['Fund_CNPF_Chara_Adj_NAV', 'Fund_Day_Yield'],
    #     start=date(2023, 3, 1),
    #     end=date(2023, 3, 29),
    #     securities=['idx_000001', 'idx_000002']
    # )
    # print(result)

    # idx_000001 = result['Fund_Day_Yield'].tolist()

    #
    # daily_value = engine.daily_factor.query_daily_factor(
    #     table_name="aShare_private_funds",
    #     factor_codes=['Fund_Day_Yield'],
    #     start=date(2023, 3, 13),
    #     end=date(2023, 3, 21),
    #     securities=['SVJ534']
    # )
    #
    # print(daily_value)

    # daily_value = engine.daily_factor.query_daily_factor(
    #
    #     table_name="aShare_funds",
    #     factor_codes=['Fund_Day_Yield', 'Return_Monthly', 'var_daily_1m', 'return_std_daily_1m', 'kurtosis_daily_1m',
    #                   'trackingerror_daily_1m', 'targetvol_daily_1m', 'sotino_daily_1m',
    #                   'skewness_daily_1m', 'winratio_monthly_1m', 'upward_captureratioreturn_daily_sinceyear',
    #                   ],
    #     start=date(2023, 2, 20),
    #     end=date(2023, 3, 20),
    #     securities=['000001']
    # )
    # Fund_Day_Yield = daily_value['Fund_Day_Yield'].tolist()
    # Fund_CNPF_NAV_Return_1M = cum(result['Fund_Day_Yield'].tolist())
    # g_avg_return_t = math.pow(g_avg_return_t(result['Fund_Day_Yield'].tolist()) + 1, 250) - 1
    # return_std_daily_1m = std(daily_value['Fund_Day_Yield'].tolist())
    # annual_return_std_daily_1m = return_std_daily_1m * 250**0.5
    # kurtosis_daily_1m = kurt(daily_value['Fund_Day_Yield'].tolist())
    # skewness_daily_1m = skew(daily_value['Fund_Day_Yield'])
    # Return_Monthly = daily_value['Return_Monthly'].tolist()
    #
    # var_daily_1m = None
    #
    # print(daily_value)
    # print('kurtosis_daily_1m', var_daily_1m)
    # #
    macro_client = engine.macro
    # # # # # #
    # # ["macro_cost_risk_free", 'Index_Return',
    # #                                                                'Index_Return_Monthly']
    macro_value = macro_client.query_by_days("aShare_macros", ['Index_Return_Weekly', 'macro_cost_risk_free'],
                                        date_generate("2023-04-01", "2023-05-09"))

    print(macro_value)
    # # #
    # index_return = macro_value['value_Index_Return'].tolist()
    #
    # day_macro_cost_risk_free = macro_value['day_Index_Return'].tolist()
    # # #
    # # # print(len(index_return), len(idx_000001))
    # # # expect = linregress(index_return, idx_000001)
    # # # print(expect)
    # #
    # # print(returns / index_return - 1)
    # #
    # macro_cost_risk_free = macro_value['value_macro_cost_risk_free'].tolist()
    # t = [i - j for i, j in zip(index_return, macro_cost_risk_free)]
    #
    # print(len(t))
    # print(len(excess_day_yield))
    # print(excess_day_yield)
    # actual_alpha_daily_1y = linregress(t, excess_day_yield)
    # print(actual_alpha_daily_1y)

    # Index_Return_Monthly = macro_value['value_Index_Return_Monthly'].tolist()
    # Index_Return = macro_value['value_Index_Return'].tolist()
    # t = [i for i, j in zip(Return_Monthly, Index_Return_Monthly) if i > j]
    # t = [a - b for a, b in zip(daily_value['Fund_Day_Yield'], macro_value['value_macro_cost_risk_free'])]
    # sharpe_daily_1m = np.mean(t) / return_std_daily_1m
    # winratio_monthly_1m = len(t) / len(Return_Monthly)
    # trackingerror_daily_1m = std([i - j for i, j in zip(Fund_Day_Yield, Index_Return)])
    # print(trackingerror_daily_1m)

    # print(Return_Monthly)
    # print(Index_Return_Monthly)

    # print(fund_day_yield - index_return)
    #
    # print(sharpe_daily_1m)

    # #
    # rr = engine.portfolio.floor_query_net_like(
    #     table_name="aShare_portfolios_fund",
    #     portfolio_id="testportfolio79908667360990",
    #     net_like_cols=['Fund_Day_Yield'],
    #     query_date=date(2023, 3, 27)
    # )
    #
    # print(rr)
    # # #

    #
    # # trading_date = engine.trading_day.query_all_trading_day(table_name="aShare_funds")
    # # print(trading_date)
    # #
    # # trading_date = engine.trading_day.query_all_trading_day(table_name="aShare_benchmarks")
    # # print(trading_date['vec'])
    # #
    # # trading_date = engine.trading_day.query_all_trading_day(table_name='aShare_private_funds')
    # # print(trading_date)
    # #
    # # # index_factor = engine.daily_factor.query_daily_factor(
    # # #     table_name="aShare_benchmarks",
    # # #     factor_codes=['abexcess_ret_wmd'],
    # # #     start=date(2023, 1, 2),
    # # #     end=date(2023, 2, 2),
    # # #     securities=['idx_000001sh']
    # # # )
    # #
    # # # print(index_factor)
    # # #
    # # index_macro = engine.macro.query_by_offset(
    # #     table_name="aShare_index",
    # #     macro_codes=['debt_convertible_daily_test'],
    # #     base=date(2023, 2, 8),
    # #     pre_offset=-1
    # # )
    # # print(index_macro)
    # #
    # # result = engine.identity.query_all_identity(table_name="aShare_benchmarks")
    # #
    # # print(result['code'].tolist())
    #
    # # identity = engine.identity.query_all_identity_by_codes(table_name="aShare_private_funds", identity_codes=['HF00000029'])
    # #
    # # print(identity)
    # #
    # # funds = result['code'].tolist()
    # #
    # # print('barbeyond benchmarks code :', len(funds), funds)
    # # result = engine.identity.query_all_identity(table_name="aShare_funds")
    # # funds = result['code']
    #
    #
    # # codes= []
    # # with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/aShare_benchmarks_identity.txt', 'r') as f:
    # #     lines = f.readlines()
    # #     for line in lines:
    # #         codes.append(line.strip('\n'))
    # #
    # # other = []
    # # for i in benchmarks:
    # #     if i not in codes:
    # #         other.append(i)
    # #
    # # print(len(other), other)
    #
    #
    # # print(len([i for i in result['endDate'] if i is None]))
    #
    #
    # # # 股池
    # # unv = engine.universe.query_universe_by_date_range(
    # #     universe_table_name='funds',
    # #     universe_code='allFund',
    # #     from_date=date(2019, 9, 11),
    # #     to_date=date(2023, 3, 22)
    # # )
    # # result = unv['identity']
    # # print(result)
    # # for item in result:
    # #     if 'HF0000A7DI' == item:
    # #         print(item, '存在')
    # #         break
    # # else:
    # #     print('不存在')
    #
    # # 稀疏数据
    #
    # # sparse_value = engine.sparse.single_date.query_data_by_offset(
    # #     table='aShare_funds_month',
    # #     factor_cols=['return_std_daily_wmd'],
    # #     query_date=date(2023, 3, 20),
    # #     pre_offset=0
    # # )
    # #
    # # print(sparse_value)
    #
    # #
    # # 生产环境
    # # dag: identity, trading_date,
    #
    # all = engine.trading_day.query_all_trading_day(table_name="aShare_bonds")
    # print(all)
    #
    # all = engine.trading_day.query_all_trading_day(table_name="aShare_private_funds")
    # print(all)

    net_like = engine.portfolio.floor_query_net_like(
        table_name="aShare_portfolios_fund",
        portfolio_id="tof_case_18",
        net_like_cols=["Fund_CNPF_Chara_Adj_NAV", "Fund_Day_Yield", "cash", "cashWeight"],
        query_date=date(2022, 3, 14),
    )
    print(net_like)

    position = engine.portfolio.floor_query_position(
        table_name="aShare_portfolios_fund",
        portfolio_id="tof_case_18",
        position_cols=["weight"],
        query_day=date(2022, 3, 14),
    )
    print(position)

# 生产环境有问题的组合: 21063, 21100, 21103, 21104, 21105