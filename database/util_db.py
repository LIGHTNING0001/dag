import pymysql

host = '192.168.194.241'
port = 3306
username = 'root'
password = 'beifa888'

need_init_history = {
    'negative_day_yield_pick': '2005-01-04',
    'positive_day_pick': '2005-01-04',
    'negative_day_reverse': '2005-01-04',
    'negative_month_yield_pick': '2005-01-04',
    'negative_week_yield_pick': '2005-01-04',
    'delete_fund_neg_day_yield': '2005-01-04',
    'day_r_square_sum_1wy': '2005-01-04',
    'day_r_square_sum_1wm': '2005-01-04',
    'excess_risk_free_square': '2005-01-04',
    'excess_day_yield': '2005-01-04'
}

need_daily_gen = {
    'avg_loss_daily_sincetotal': '2023-04-06',
    'downrisk_monthly_sincetotal': '2023-04-06',
    'neg_reverse_sum_5y': '2023-04-06',
    'pos_sum_5y': '2023-04-06',
    'downrisk_daily_sincetotal': '2023-04-06',
    'downrisk_weekly_sincetotal': '2023-04-06',
    'avg_profit_daily_sincetotal': '2023-04-06',
    'stock_selectabilty_daily_sincetotal': '2023-04-06',
    'month_r_square_sum_sincetotal': '2023-04-06',

}


def init_history():
    db = pymysql.connect(host=host, port=port, user=username, password=password)
    cursor = db.cursor()

    for k, v in need_init_history.items():
        # 删除 t_scheduler_data_update_result 的记录
        sql = "delete from jictrust_saas.t_scheduler_data_update_result where subject = 'open_fund.factor.{}'".format(k)
        cursor.execute(sql)
        db.commit()

        # 更新 t_data_logic_table_col
        sql = "update jictrust_saas.t_data_logic_table_col set init_start = '{}', `start` = null, `end` = null where full_code  = 'open_fund.factor.{}'".format(v, k)
        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()


def daily_gen():
    db = pymysql.connect(host=host, port=port, user=username, password=password)
    cursor = db.cursor()

    for k, v in need_init_history.items():
        # 删除 t_scheduler_data_update_result 的记录
        sql = "update jictrust_saas.t_scheduler_data_update_result set `to` = '{}' where subject = 'index.factor.{}' and `to` = '2023-04-07';".format(v, k)
        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()


if __name__ == '__main__':
    # init_history()
    daily_gen()






