
from datetime import date

from calculator.formula import cum
from client.grpc_client import engine


def test_1():
    base_factor = 'Fund_Day_Yield'
    exp_factor = engine.daily_factor.query_daily_factor(
        table_name='aShare_funds',
        factor_codes=[base_factor],
        start=date(2023, 1, 27),
        end=date(2023, 2, 2),
        securities=['000001_OF'])[base_factor].array
    expect = cum(exp_factor)
    factor = 'Return_Weekly'
    actual = engine.daily_factor.query_daily_factor(
        table_name='aShare_funds',
        factor_codes=[factor],
        start=date(2023, 2, 2),
        end=date(2023, 2, 2),
        securities=['000001_OF'])[factor].tolist()[-1]

    assert round(expect, 6) == round(actual, 6), '{0} check fail'.format(factor)

