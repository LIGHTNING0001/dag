
from datasource.mysql_db import query, upsert

datasource = '2023-02-07'

def test_db():
    result_set = query("select * from barbeyond.t_data_logic_table_col")
    print(result_set)

    # 检查mysql表里因子的end时间(col表和result表)
    for row in result_set:
        pass

    codes = []
    for full_code in codes:
        items = query("select item, `to` from barbeyond.t_schedular_data_update_result where subject={}".format(full_code))

        for item in items:
            pass

    # 对 `to` 进行检验
    # 检验因子值从两个方面验证：1. 判断是否算出来。2. 判断值正确性（不好实现）


    # 检查 barbyond 因子的 meta, 通过查询因子判断（增量更新一天的）
    # 通过因子查询所有item


    # upsert(
    #     "update barbeyond.t_data_logic_table_col set init_start = '2023-01-03' where full_code = 'stock.factor.annual_return_std_monthly_1m'")
    #