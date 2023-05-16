from datetime import date

from calculator.formula import kurt
from client.grpc_client import engine


def test_1():
    base_factor = 'Return_Weekly'
    exp_factor = engine.daily_factor.query_daily_factor(
        table_name='aShare_benchmarks',
        factor_codes=[base_factor],
        start=date(2023, 1, 3),
        end=date(2023, 2, 2),
        securities=['idx_000001sh'])
    print('\n', exp_factor)
    expect = kurt(exp_factor[base_factor].array)
    factor = 'kurtosis_weekly_1m'
    result = engine.daily_factor.query_daily_factor(
        table_name='aShare_benchmarks',
        factor_codes=[factor],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['idx_000001sh'])
    print('\n', result)
    actual = result[factor].tolist()[-1]

    assert round(expect, 6) == round(actual, 6), '{0} check fail'.format(factor)
