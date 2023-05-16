import pymysql
import paramiko

host = '192.168.0.113'
port = 3306
username = 'root'
password = 'beifa888'

path = '/home/betalpha/app/jar/cluster_server/data/cache/daily_factor/aShare_stocks_daily_factor/upload-zone/identity'

trans = paramiko.Transport(("192.168.0.112", 22))
trans.connect(username="betalpha", password="bfisnotgf")

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
command = "cat {}".format(path)
print(command)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)

lines = ssh_stdout.readlines()

identities = [i.rstrip('\n') for i in lines]

print(identities)

# 关闭连接
trans.close()

db = pymysql.connect(host=host, port=port, user=username, password=password)
cursor = db.cursor()

def read_csv():
    pass


def insert_day_yield_to_result():
    for identity in identities:
        items = identity.split(',')
        item = items[0]
        start_date = items[1]
        end_date = '2023-03-07' if items[2] == '' else items[2]

        sql = "insert into barbeyond.t_scheduler_data_update_result values('stock.factor.Day_Yield', '{}', '{}', '{}', '1680092558802', '1680092558802')".format(
            item, start_date, end_date)

        cursor.execute(sql)
        db.commit()
    cursor.close()
    db.close()


insert_day_yield_to_result()


# def add_meta_factor():
#
#     lines = read_csv()







