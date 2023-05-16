from datetime import date

from calculator.formula import skew
from client.grpc_client import engine
import logging


# def test_1():
#
#     base_factor = 'Return_Weekly'
#     exp_factor = engine.daily_factor.query_daily_factor(
#         table_name='aShare_benchmarks',
#         factor_codes=[base_factor],
#         start=date(2023, 1, 3),
#         end=date(2023, 2, 2),
#         securities=['idx_000001sh'])
#     print('\n', exp_factor)
#     expect = skew(exp_factor[base_factor].array)
#     factor = 'skewness_weekly_1m'
#     result = engine.daily_factor.query_daily_factor(
#         table_name='aShare_benchmarks',
#         factor_codes=[factor],
#         start=date(2023, 2, 2),
#         end=date(2023, 2, 2),
#         securities=['idx_000001sh'])
#     print('\n', result)
#     actual = result[factor].tolist()[-1]
#
#     assert round(expect, 6) == round(actual, 6), '{0} check fail'.format(factor)
r = []

with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/skew_data/skew_data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        r.append(float(line.strip('\n')))

result = skew(r)

print(result)
