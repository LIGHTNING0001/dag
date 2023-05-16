from calculator.formula import linregress

returns = []
index = []

with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/alpha_beta/returns.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        returns.append(float(line.strip('\n')))


with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/alpha_beta/index.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        index.append(float(line.strip('\n')))

print(returns)
print(index)

alpha, beta = linregress(index, returns)

print(alpha, beta)
