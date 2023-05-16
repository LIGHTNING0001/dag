import math

from calculator.formula import g_avg_return_t

returns = []

with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/data1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        returns.append(float(line.strip('\n')))


expect_value = math.pow(g_avg_return_t(returns) + 1, 250) - 1

print(expect_value)

