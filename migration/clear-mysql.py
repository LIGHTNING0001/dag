
import pymysql


host = '192.168.0.100'
port = 50405
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
        sql = 'delete from jictrust_betalpha.asset_factor_copy where code like "{}%"'.format(factor)

        cursor.execute(sql)
        db.commit()


clear_asset_factor()




