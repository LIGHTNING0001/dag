from selenium.webdriver.common.by import By

create_dag_item = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/span/button/span')

dag_name_ipt = (By.ID, 'saveDagForm_dagName')

ack_dag = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button[2]')

model_tab = (By.XPATH, '/html/body/div/div/div[1]/div[2]/ul/li[4]/span')

run_dag = (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/div[2]/span/button')

select_logo = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/span[2]')

all = (By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div/div[3]/div/div')

# /html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/button
look_btn = (By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/div[1]/button')

# 添加元数据节点
add_meta_data = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/span/button')


# 新建元数据节点
new_meta_data = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/span/span')

# 命名空间
namespace_input = (By.ID, 'saveDagForm_namespace')

# 默认分类
default_category = (By.XPATH, '/html/body/div[4]/div/div/div/div/ul/li/div[1]')

stock_tab = (By.XPATH, '/html/body/div[4]/div/div/div/div/ul[2]/li[2]/div[1]')

# /html/body/div[3]/div/div/div/div/ul[3]/li[1]/div[1]
stock_factor = (By.XPATH, '/html/body/div[4]/div/div/div/div/ul[3]/li[1]')

stock_factor_1 = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul[3]/li[1]/div[1]')

# 物理表
physical_table = (By.ID, 'saveDagForm_physicsTableCode')
barbeyond_store = (By.XPATH, '/html/body/div[5]/div/div/div/div/ul/li/div[1]')
stock_daily_factor = (By.XPATH, '/html/body/div[5]/div/div/div/div/ul[2]/li[2]')
stock_month_factor = (By.XPATH, '/html/body/div[5]/div/div/div/div/ul[2]/li[11]')
stock_year_factor = (By.XPATH, '/html/body/div[5]/div/div/div/div/ul[2]/li[12]')

# 名称
saveDagForm_name = (By.ID, 'saveDagForm_name')
saveDagForm_code = (By.ID, 'saveDagForm_code')

# 公式输入框
formula = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div[2]/div/div/div/div[2]/div')

# 确认按钮
submit_btn = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]')


# 添加元素到dag 里面
meta_data = (By.ID, 'saveDagForm_metaData')

new_meta_data_1 = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/span/button')

default_category_1 = (By.XPATH, '/html/body/div[4]/div/div/div/div/ul/li')

stock_item = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul[2]/li[2]/div[1]')

jobType = (By.ID, 'saveDagForm_jobType')

embed_formula = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[1]/div')


None_category = (By.XPATH, '/html/body/div[3]/div/div/div/div/ul/li/div[1]')


add_meta_data_submit = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
cancell_button = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]/span')


#
# /home/betalpha/app/jdk/jdk-11.0.2/bin/java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5054 -DisOffline=true -Dgrpc.server.fileName=./cluster_server.toml -Ddag.cluster.role=WORKER -Ddag.cluster.seedsHostPort=192.168.0.114:2499 -Dloader.path=/thirdparty/mosek/ -Djava.library.path=/thirdparty/mosek/ -Dcass.datasource=false -Duse.data.store=barbeyond -Dspring.profiles.active=distributed -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.rmi.port=9998 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dsaas.barbeyond.cluster.server=192.168.0.113:8882 -Dsaas.barbeyond.cluster.servers=192.168.0.112:8881,192.168.0.113:8882,192.168.0.114:8883 -Dsaas.barbeyond.cluster.metaDir=/home/betalpha/app/jar/cluster_server/data --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED -jar bar-svc-api-app-1.1.0-SNAPSHOT.jar
# /home/betalpha/app/jdk/jdk-11.0.2/bin/java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5054 -DisOffline=true -Duse.data.store=barbeyond -Dgrpc.server.fileName=./cluster_server.toml -Dloader.path=/thirdparty/mosek/ -Djava.library.path=/thirdparty/mosek/ -Dcass.datasource=false -Duse.data.store=barbeyond -Dspring.profiles.active=distributed -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.rmi.port=9998 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dsaas.barbeyond.cluster.server=192.168.0.112:8881 -Dsaas.barbeyond.cluster.servers=192.168.0.112:8881,192.168.0.113:8882,192.168.0.114:8883 -Dsaas.barbeyond.cluster.metaDir=/home/betalpha/app/jar/cluster_server/data -Ddag.cluster.role=WORKER -Ddag.cluster.seedsHostPort=192.168.0.114:2499 --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED -jar bar-svc-api-app-1.1.0-SNAPSHOT.jar
# /home/betalpha/app/jdk/jdk-11.0.2/bin/java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5054 -DisOffline=true -Dgrpc.server.fileName=./cluster_server.toml -Ddag.cluster.role=MASTER -Ddag.cluster.seedsHostPort=192.168.0.114:2499 -Dloader.path=/thirdparty/mosek/ -Djava.library.path=/thirdparty/mosek/ -Dcass.datasource=false -Duse.data.store=barbeyond -Dspring.profiles.active=distributed -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.rmi.port=9998 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Dsaas.barbeyond.cluster.server=192.168.0.114:8883 -Dsaas.barbeyond.cluster.servers=192.168.0.112:8881,192.168.0.113:8882,192.168.0.114:8883 -Dsaas.barbeyond.cluster.metaDir=/home/betalpha/app/jar/cluster_server/data --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED -jar bar-svc-api-app-1.1.0-SNAPSHOT.jar