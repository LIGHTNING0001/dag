import datetime
from datetime import time

from dateutil.relativedelta import relativedelta


from common.flight_utils import SchemaCol
from sdk.client_builder import create_grpc_sdk

import pandas as pd

# http://119.3.25.25:30054/
username = 'admin'
password = 'secret'
host = '192.168.0.114'
port = 50053

engine = create_grpc_sdk(username=username, password=password, host=host, port=port)


for i in range(1):
    factor = ['factor_3']

    engine.sparse.single_date.create_table(
        table="test_performance1",
        factor_cols=factor
    )

    row = []
    base_date = '2020-12-31'
    for j in range(12):
        dt = datetime.datetime.strptime(base_date, "%Y-%m-%d")
        for k in range(2000):
            r = (str(k), dt, 0.1)
            row.append(r)
        base_date = (dt + relativedelta(months=1)).strftime("%Y-%m-%d")

    data = pd.DataFrame.from_records(
        row, columns=['identity', SchemaCol.date] + factor)

    print(data)


    engine.sparse.single_date.update_data(
        table='test_performance',
        factor_cols=factor,
        data_df=data,
    )



if __name__ == '__main__':
    pass