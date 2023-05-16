import math
from datetime import date

import numpy as np

from calculator.formula import linregress, g_avg_return_t, maxdrawdown_t, cum, std
from client.grpc_client import engine, date_generate


def test_linregress():
    macro_client = engine.macro

    index_return = macro_client.query_by_days("aShare_macros", ["Index_Return"],
                                              date_generate("2023-01-03", "2023-02-02"))

    print(index_return)
    fund_day_yield = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_Day_Yield'],
        start=date(2023, 1, 3),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(fund_day_yield)

    expect_alpha = linregress(index_return['value_Index_Return'].tolist(),
                              fund_day_yield['Fund_Day_Yield'].tolist())
    print("预期：", expect_alpha)

    actual_alpha = engine.daily_factor.query_daily_factor(
        table_name='aShare_funds',
        factor_codes=['alpha_daily_1m'],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    actual_bet = engine.daily_factor.query_daily_factor(
        table_name='aShare_funds',
        factor_codes=['bet1'],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )

    print("实际：", actual_alpha)
    print(actual_bet)


def test_g_avg_return_t():
    fund_day_yield = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_Day_Yield'],
        start=date(2023, 1, 3),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(fund_day_yield)
    expect_value = math.pow(g_avg_return_t(fund_day_yield['Fund_Day_Yield'].tolist()) + 1, 250) - 1
    print("预期", expect_value)

    actual_value = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['annual_ret_daily_1m_test'],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(actual_value)
    print("实际", actual_value['annual_ret_daily_1m_test'][0])
    assert expect_value == actual_value, 'annual_ret_daily_1m,结果与预期不符'


def test_maxdrawdown_t():
    fund_day_yield = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_Day_Yield'],
        start=date(2023, 1, 3),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(fund_day_yield)

    macro_client = engine.macro

    index_return = macro_client.query_by_days("aShare_macros", ["Index_Return"],
                                              date_generate("2023-01-03", "2023-02-02"))
    print(index_return)

    n_arr = [i - j for i, j in zip(fund_day_yield['Fund_Day_Yield'].tolist(), index_return['value_Index_Return'].tolist())]

    expect_value = maxdrawdown_t(n_arr)

    actual_value = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['excess_maxdrawdown_1m_test'],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )['excess_maxdrawdown_1m_test'][0]
    print(fund_day_yield)
    print(expect_value, actual_value)
    assert actual_value == expect_value, 'excess_maxdrawdown_1m_test, 与预期结果不符'


def test_std_t():
    fund_day_yield = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['Fund_Day_Yield'],
        start=date(2023, 1, 3),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(fund_day_yield['Fund_Day_Yield'].tolist())

    expect = std(fund_day_yield['Fund_Day_Yield'].tolist())
    print(np.var(fund_day_yield['Fund_Day_Yield'].tolist()))

    actual = engine.daily_factor.query_daily_factor(
        table_name="aShare_funds",
        factor_codes=['return_std_daily_1m_test'],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF']
    )
    print(actual)

    assert actual['return_std_daily_1m_test'][0] == expect



def test_avg_t():
    pass
