import yaml

def parse(file):
   with open(file, 'r') as f:
       data = yaml.load(f, Loader=yaml.FullLoader)
       print(data)


if __name__ == '__main__':
    parse("/Users/mac/PycharmProjects/dag_v2_test/testcase/tof.yaml")
