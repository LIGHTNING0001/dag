import pymysql

host = '192.168.194.242'
port = 3306
username = 'root'
password = 'beifa888'

db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()


def read_factor_like():
    factors = []
    with open('clear_barbeyond.sh', 'r') as f:
        lines = f.readlines()
        for line in lines:
            t = line.split(' ')
            factors.append(t[5].lstrip('\'').rstrip('*\''))

    return factors

print(read_factor_like())


def clear_asset_factor():
    factors = read_factor_like()
    for factor in factors:
        sql = 'delete from jictrust_betalpha.asset_factor where code like "{}%"'.format(factor)

        cursor.execute(sql)
        db.commit()

# clear_asset_factor()


def clear_result():
    sql = "delete from jictrust_saas.t_scheduler_data_update_result where subject not in ('index.factor.Fund_Day_Yield', 'index.factor.Fund_CNPF_Chara_Adj_NAV', 'index.macro.macro_cost_risk_free', 'open_fund.factor.Fund_Day_Yield', 'open_fund.factor.Fund_CNPF_Chara_Adj_NAV','open_fund.portfolio.Fund_Day_Yield', 'open_fund.portfolio.Fund_CNPF_Chara_Adj_NAV');"

    cursor.execute(sql)
    db.commit()

clear_result()

cursor.close()
db.close()



# 顶点升级最新版因子
# 1. 清除之前barbeyond (指数日频因子，基金日频因子，删除组合表，重启服务器)
# 2. 升级 gen
# 2. 升级 mig



