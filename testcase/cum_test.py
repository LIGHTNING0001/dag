from calculator.formula import cum

rr = []

with open('/Users/mac/PycharmProjects/dag_v2_test/testcase/data/cummula_data/data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        rr.append(float(line.strip('\n')))

print(cum(rr))